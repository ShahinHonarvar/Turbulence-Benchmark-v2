def palindromes_between_indices(s):
    s = s[:4].lower()
    letters = [c for c in s if c.isalpha()]
    palindromes = set()
    for i in range(len(letters)):
        for j in range(i + 1, len(letters)):
            for k in range(j, len(letters)):
                for l in range(k + 1, len(letters)):
                    word = letters[i] + letters[j] + letters[k] + letters[l]
                    if word == word[::-1]:
                        palindromes.add(word)
    return palindromes