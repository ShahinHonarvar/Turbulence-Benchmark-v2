def palindromes_of_specific_lengths(s):
    s = s[29:97]
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + 12, min(i + 19, len(s) + 1)):
            substring = s[i:j]
            clean_substring = ''.join(filter(str.isalpha, substring)).lower()
            if len(clean_substring) >= 12 and clean_substring == clean_substring[::-1]:
                palindromes.add(clean_substring)
    return palindromes