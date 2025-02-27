def palindromes_of_specific_lengths(s):
    s = s[23:78]
    palindromes = set()
    for start in range(len(s)):
        for length in range(13, 41):
            end = start + length
            if end > len(s):
                break
            substring = s[start:end]
            filtered_substring = ''.join(filter(str.isalpha, substring)).lower()
            if filtered_substring == filtered_substring[::-1] and len(filtered_substring) == length:
                palindromes.add(substring)
    return palindromes