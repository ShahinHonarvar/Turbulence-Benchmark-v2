def palindromes_between_indices(s):
    s = s[0:4].lower()
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + 2, len(s) + 1):
            substring = s[i:j]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes