def palindromes_of_specific_lengths(s):
    s = s[10:71]
    palindromes = set()
    for len in range(24, 53):
        for i in range(len, len(s) - len + 1):
            substring = s[i - len:i + len]
            substring = substring.lower()
            if all((c.isalpha() for c in substring)) and substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes