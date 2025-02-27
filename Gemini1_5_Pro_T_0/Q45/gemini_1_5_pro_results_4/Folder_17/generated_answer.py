def palindromes_between_indices(string):
    letters = []
    for i in range(2, 7):
        if string[i].isalpha():
            letters.append(string[i].lower())
    result = set()
    for i in range(len(letters)):
        for j in range(i + 1, len(letters)):
            for k in range(j + 1, len(letters)):
                for l in range(k + 1, len(letters)):
                    temp = [letters[i], letters[j], letters[k], letters[l]]
                    for permutation in range(24):
                        word = ''.join(temp)
                        if word == word[::-1] and len(word) >= 4:
                            result.add(word)
                        temp = [temp[1], temp[0], temp[3], temp[2]]
                        word = ''.join(temp)
                        if word == word[::-1] and len(word) >= 4:
                            result.add(word)
                        temp = [temp[2], temp[1], temp[0], temp[3]]
                        word = ''.join(temp)
                        if word == word[::-1] and len(word) >= 4:
                            result.add(word)
    return result