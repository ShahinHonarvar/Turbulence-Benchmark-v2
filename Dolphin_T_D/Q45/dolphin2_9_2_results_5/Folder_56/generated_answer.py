def palindromes_between_indices(s):
    chars = [char.lower() for char in list(s[5:10])]
    palindromes = set()
    for i in range(5, len(s)):
        for j in range(i + 2, len(s) + 1):
            substring = s[i:j]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes