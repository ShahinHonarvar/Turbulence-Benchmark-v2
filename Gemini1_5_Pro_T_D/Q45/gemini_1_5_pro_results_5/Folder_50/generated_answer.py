def palindromes_between_indices(string):
    letters = ''.join((char.lower() for char in string[4:9] if char.isalpha()))
    palindromes = set()
    for i in range(len(letters) - 4):
        for j in range(i + 5, len(letters) + 1):
            substring = letters[i:j]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes