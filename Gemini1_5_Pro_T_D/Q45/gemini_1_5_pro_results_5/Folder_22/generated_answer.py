def palindromes_between_indices(string):
    letters = ''.join((char for char in string[5:7] if char.isalpha())).lower()
    if len(letters) < 3:
        return set()
    result = set()
    for i in range(len(letters) - 2):
        for j in range(i + 1, len(letters) - 1):
            for k in range(j + 1, len(letters)):
                current = letters[i] + letters[j] + letters[k]
                if current == current[::-1]:
                    result.add(current)
    return result