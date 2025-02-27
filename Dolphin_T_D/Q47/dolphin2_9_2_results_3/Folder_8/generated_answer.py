def palindromes_of_specific_lengths(s):
    s = s[16:73]
    palindromes = set()
    for i in range(50, 52):
        for j in range(len(s) - i + 1):
            substring = s[j:j + i]
            if substring == substring[::-1] and all((c.isalpha() for c in substring.lower())):
                palindromes.add(substring)
    return palindromes