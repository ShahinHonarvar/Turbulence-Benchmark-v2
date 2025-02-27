def palindromes_between_indices(s):
    letters = s[1:9].lower()
    palindromes = set()
    for i in range(len(letters)):
        for j in range(i, len(letters)):
            substring = letters[i:j + 1]
            if len(substring) >= 6 and substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes