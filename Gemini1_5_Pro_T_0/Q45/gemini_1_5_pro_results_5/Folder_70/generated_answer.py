def palindromes_between_indices(string):
    letters = ''.join((c for c in string[1:7] if c.isalpha())).lower()
    result = set()
    for i in range(len(letters) - 3):
        for j in range(i + 3, len(letters) + 1):
            substring = letters[i:j]
            if substring == substring[::-1]:
                result.add(substring)
    return result