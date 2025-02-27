def palindromes_between_indices(s):
    letters = s[2:4].lower()
    if len(set(letters)) != len(letters):
        return set()
    length = len(letters)
    if length < 3:
        return set()
    palindromes = set()
    for i in range(length):
        for j in range(i + 1, length):
            substring = letters[i:j + 1]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes