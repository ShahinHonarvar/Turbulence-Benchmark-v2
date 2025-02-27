def palindromes_between_indices(string):
    letters = []
    for i in range(1, 7):
        if string[i].isalpha():
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
                                    temp = letters[i:j] + letters[k:l] + letters[m:n] + letters[o:p]
                                    if len(temp) >= 7:
                                        if temp == temp[::-1]:
                                            result.add(''.join(temp))
    return result