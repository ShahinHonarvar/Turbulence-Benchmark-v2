def palindromes_of_specific_lengths(s):
    s = s[:101]
    s = ''.join(filter(str.isalpha, s)).lower()
    palindromes = set()
    for start in range(len(s)):
        for end in range(start + 2, min(start + 15, len(s) - 1) + 1):
            substring = s[start:end + 1]
            if substring == substring[::-1] and 3 <= len(substring) <= 15:
                palindromes.add(substring)
    return palindromes