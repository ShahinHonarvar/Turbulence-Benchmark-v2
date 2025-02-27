def palindromes_between_indices(string):
    letters = []
    for i in range(2, 5):
        if string[i].isalpha():
            letters.append(string[i].lower())
    result = set()
    if len(letters) >= 3:
        for i in range(len(letters)):
            for j in range(i + 1, len(letters)):
                for k in range(j + 1, len(letters)):
                    s = letters[i] + letters[j] + letters[k]
                    if s == s[::-1]:
                        result.add(s)
    return result