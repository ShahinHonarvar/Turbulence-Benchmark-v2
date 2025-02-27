def palindromes_between_indices(string):
    letters = ''.join((char.lower() for char in string[3:9] if char.isalpha()))
    result = set()
    for i in range(len(letters) - 3):
        for j in range(i + 3, len(letters) + 1):
            substring = letters[i:j]
            if substring == substring[::-1]:
                result.add(substring)
    return result