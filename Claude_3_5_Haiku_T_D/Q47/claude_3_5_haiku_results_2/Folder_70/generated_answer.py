def palindromes_of_specific_lengths(s):
    palindromes = set()
    s = s.lower()
    for start in range(10, 71):
        for end in range(start + 23, min(71, len(s) + 1)):
            substring = s[start:end]
            if len(substring) >= 24 and len(substring) <= 52:
                if substring == substring[::-1] and substring.isalpha():
                    palindromes.add(substring)
    return palindromes