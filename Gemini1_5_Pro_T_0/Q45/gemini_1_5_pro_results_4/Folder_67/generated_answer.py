def palindromes_between_indices(string):
    letters = []
    for i in range(2, 7):
        if 97 <= ord(string[i].lower()) <= 122:
            letters.append(string[i].lower())
    result = set()
    for i in range(len(letters) + 1):
        for j in range(i + 1, len(letters) + 1):
            for k in range(j + 1, len(letters) + 1):
                for l in range(k + 1, len(letters) + 1):
                    for m in range(l + 1, len(letters) + 1):
                        temp = letters[i:j] + letters[j:k] + letters[k:l] + letters[l:m] + letters[m:]
                        if len(temp) >= 5:
                            if temp == temp[::-1]:
                                result.add(''.join(temp))
    return result