def palindromes_of_specific_lengths(s):
    s = s.lower()
    valid_palindromes = set()
    for start in range(65, 100):
        for length in range(26, 34):
            end = start + length
            if end <= 100:
                substring = s[start:end]
                filtered_substring = ''.join(filter(str.isalpha, substring))
                if len(filtered_substring) == length and filtered_substring == filtered_substring[::-1]:
                    valid_palindromes.add(filtered_substring)
    return valid_palindromes