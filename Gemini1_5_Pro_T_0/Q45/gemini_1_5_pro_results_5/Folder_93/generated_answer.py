def palindromes_between_indices(string):
    letters = ''.join((char for char in string[2:8] if char.isalpha())).lower()
    result = set()
    for i in range(len(letters) + 1):
        for j in range(i + 6, len(letters) + 1):
            substring = letters[i:j]
            if substring == substring[::-1]:
                result.add(substring)
    return result