def palindromes_of_specific_lengths(s):
    s = s[:101]
    n = len(s)
    palindromes = set()
    for i in range(n):
        for j in range(i + 2, min(i + 15, n) + 1):
            substring = s[i:j]
            clean_substring = ''.join(filter(str.isalpha, substring)).lower()
            if len(clean_substring) >= 3 and clean_substring == clean_substring[::-1]:
                palindromes.add(clean_substring)
    return palindromes