def palindromes_between_indices(string):
    letters = ''.join((letter.lower() for letter in string[2:6] if letter.isalpha()))
    if len(letters) < 5:
        return set()
    palindromes = set()
    for i in range(len(letters) - 4):
        for j in range(i + 4, len(letters)):
            substring = letters[i:j + 1]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes