def palindromes_of_specific_lengths(s):
    start_index, end_index = (127, 288)
    min_len, max_len = (119, 141)
    valid_chars = [c for c in s[start_index:end_index + 1] if c.isalpha()]
    valid_string = ''.join(valid_chars).lower()
    results = set()
    for i in range(len(valid_string)):
        for length in range(min_len, max_len + 1):
            if i + length > len(valid_string):
                break
            substring = valid_string[i:i + length]
            if substring == substring[::-1]:
                original_substring_indices = []
                k = 0
                for j in range(start_index, end_index + 1):
                    if s[j].isalpha():
                        if k >= i and k < i + length:
                            original_substring_indices.append(j)
                        k += 1
                results.add(''.join((s[index] for index in original_substring_indices)))
    return results