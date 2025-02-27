def palindromes_between_indices(string):
    letters = [char.lower() for char in string[5:9]]
    palindromes = set()
    for i in range(len(letters)):
        for j in range(i + 2, len(letters) + 1):
            substring = letters[i:j]
            if substring == substring[::-1] and len(substring) >= 3:
                palindromes.add(''.join(substring))
    return palindromes