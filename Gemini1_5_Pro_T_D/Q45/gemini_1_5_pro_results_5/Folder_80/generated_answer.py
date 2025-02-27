def palindromes_between_indices(string):
    letters = []
    for i in range(3, 9):
        if 97 <= ord(string[i].lower()) <= 122:
            letters.append(string[i].lower())
    result = set()
    for i in range(len(letters) + 1):
        for j in range(i + 1, len(letters) + 1):
            for k in range(len(letters) + 1):
                for l in range(k + 1, len(letters) + 1):
                    for m in range(len(letters) + 1):
                        for n in range(m + 1, len(letters) + 1):
                            for o in range(len(letters) + 1):
                                for p in range(o + 1, len(letters) + 1):
                                    word = letters[i:j] + letters[k:l] + letters[m:n] + letters[o:p]
                                    if len(word) >= 7 and word == word[::-1]:
                                        result.add(''.join(word))
    return result