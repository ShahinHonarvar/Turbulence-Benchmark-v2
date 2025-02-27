def palindromes_of_specific_lengths(s):
    s = s[:7].lower()
    palindromes = set()
    for start in range(len(s)):
        for end in range(start + 3, min(len(s), start + 7)):
            substring = s[start:end + 1]
            if substring.isalpha() and substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes