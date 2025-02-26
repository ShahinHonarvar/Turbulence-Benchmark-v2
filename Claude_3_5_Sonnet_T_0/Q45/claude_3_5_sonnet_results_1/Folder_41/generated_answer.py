def palindromes_between_indices(s):
    letters = ''.join(filter(str.isalpha, s[2:4])).lower()
    if len(letters) < 2:
        return set()
    palindromes = set()
    for i in range(len(letters)):
        for j in range(i + 1, len(letters) + 1):
            substring = letters[i:j]
            if len(substring) >= 3 and substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes