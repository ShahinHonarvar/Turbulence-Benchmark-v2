def palindromes_of_specific_lengths(s):
    s = s[30:85].lower()
    palindromes = set()
    for start in range(len(s)):
        for end in range(start + 12, min(len(s), start + 21)):
            substring = s[start:end]
            filtered_substring = ''.join(filter(str.isalpha, substring))
            if filtered_substring == filtered_substring[::-1] and len(filtered_substring) >= 12:
                palindromes.add(filtered_substring)
    return palindromes