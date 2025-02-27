def palindromes_between_indices(string):
    letters = []
    for i in range(4, 8):
        if 97 <= ord(string[i].lower()) <= 122:
            letters.append(string[i].lower())
    result = set()
    if len(letters) >= 5:
        for i in range(len(letters)):
            for j in range(i + 1, len(letters)):
                for k in range(j + 1, len(letters)):
                    for l in range(k + 1, len(letters)):
                        for m in range(l + 1, len(letters)):
                            temp = [letters[i], letters[j], letters[k], letters[l], letters[m]]
                            for p in range(len(temp)):
                                temp1 = [temp[p]] + temp[:p] + temp[p + 1:]
                                for q in range(len(temp1)):
                                    temp2 = [temp1[q]] + temp1[:q] + temp1[q + 1:]
                                    for r in range(len(temp2)):
                                        temp3 = [temp2[r]] + temp2[:r] + temp2[r + 1:]
                                        for s in range(len(temp3)):
                                            temp4 = [temp3[s]] + temp3[:s] + temp3[s + 1:]
                                            for t in range(len(temp4)):
                                                temp5 = [temp4[t]] + temp4[:t] + temp4[t + 1:]
                                                word = ''.join(temp5)
                                                if word == word[::-1]:
                                                    result.add(word)
    return result