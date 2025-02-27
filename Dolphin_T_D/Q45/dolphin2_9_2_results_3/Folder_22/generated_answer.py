def palindromes_between_indices(s):
    letters = s[5:7]
    palindromes = set()
    for i in range(len(letters)):
        for j in range(i + 2, len(letters) + 1):
            substring = letters[i:j]
            if substring == substring[::-1]:
                palindromes.add(substring.lower())
    return palindromes