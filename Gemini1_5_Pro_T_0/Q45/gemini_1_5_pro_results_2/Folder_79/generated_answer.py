def palindromes_between_indices(string):
    letters = ''.join((c for c in string[1:8] if c.isalpha())).lower()
    result = set()
    for i in range(len(letters) + 1):
        for j in range(i + 1, len(letters) + 1):
            substring = letters[i:j]
            if len(substring) >= 3 and substring == substring[::-1]:
                result.add(substring)
    return result