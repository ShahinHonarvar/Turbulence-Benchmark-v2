def palindromes_between_indices(s):
    letters = ''.join(filter(str.isalpha, s[4:9]))
    letters = letters.lower()
    n = len(letters)
    if n < 5:
        return set()
    palindromes = set()
    for i in range(n):
        for j in range(i + 5, n + 1):
            substring = letters[i:j]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes