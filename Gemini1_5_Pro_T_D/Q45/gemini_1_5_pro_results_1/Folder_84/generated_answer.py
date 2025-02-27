def palindromes_between_indices(string):
    letters = [string[i].lower() for i in range(4, 10) if string[i].isalpha()]
    size = len(letters)
    if size < 3:
        return set()
    palindromes = set()
    for i in range(size):
        for j in range(i + 1, size):
            for k in range(j + 1, size):
                substring = letters[i] + letters[j] + letters[k]
                if substring == substring[::-1]:
                    palindromes.add(substring)
    return palindromes