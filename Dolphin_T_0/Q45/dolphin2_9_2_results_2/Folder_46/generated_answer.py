def palindromes_between_indices(s):
    letters = []
    for i in range(4, 10):
        if s[i].isalpha():
            letters.append(s[i].lower())
    if len(set(letters)) < 3:
        return set()
    palindromes = set()
    for length in range(6, 11):
        for i in range(len(letters)):
            for j in range(i + 1, len(letters)):
                for k in range(j + 1, len(letters)):
                    if len(set(letters[i:j + 1] + letters[k:k + length - j + i])) == 1:
                        palindromes.add(''.join(letters[i:j + 1] + letters[k:k + length - j + i]))
    return palindromes