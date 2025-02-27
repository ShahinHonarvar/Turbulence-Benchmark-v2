def palindromes_between_indices(string):
    letters = ''.join((char for char in string[1:10] if char.isalpha())).lower()
    result = set()
    for i in range(len(letters) + 1):
        for j in range(i + 1, len(letters) + 1):
            substring = letters[i:j]
            if len(substring) >= 7 and substring == substring[::-1]:
                result.add(substring)
    return result