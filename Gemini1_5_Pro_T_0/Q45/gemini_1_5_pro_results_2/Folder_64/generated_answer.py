def palindromes_between_indices(string):
    letters = []
    for i in range(4, 10):
        if 97 <= ord(string[i].lower()) <= 122:
            letters.append(string[i].lower())
    result = set()
    for i in range(len(letters) - 4):
        for j in range(i + 1, len(letters) - 3):
            for k in range(j + 1, len(letters) - 2):
                for l in range(k + 1, len(letters) - 1):
                    for m in range(l + 1, len(letters)):
                        s = letters[i] + letters[j] + letters[k] + letters[l] + letters[m]
                        if s == s[::-1]:
                            result.add(s)
    return result