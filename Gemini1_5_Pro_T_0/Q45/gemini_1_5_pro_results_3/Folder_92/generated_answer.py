def palindromes_between_indices(string):
    letters = ''.join((letter for letter in string[4:8] if letter.isalpha())).lower()
    result = set()
    for i in range(len(letters)):
        for j in range(i + 1, len(letters) + 1):
            substring = letters[i:j]
            if len(substring) >= 4 and substring == substring[::-1]:
                result.add(substring)
    return result