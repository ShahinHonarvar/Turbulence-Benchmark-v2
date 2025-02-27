def palindromes_between_indices(string):
    result = set()
    base_alphabet = 'abcdefghijklmnopqrstuvwxyz'
    for i in range(2, 10):
        for j in range(i, 10):
            for k in range(j, 10):
                for l in range(k, 10):
                    for m in range(l, 10):
                        for n in range(m, 10):
                            for o in range(n, 10):
                                for p in range(o, 10):
                                    temp = ''
                                    temp += string[p]
                                    temp += string[o]
                                    temp += string[n]
                                    temp += string[m]
                                    temp += string[l]
                                    temp += string[k]
                                    temp += string[j]
                                    temp += string[i]
                                    temp = temp.lower()
                                    if temp in base_alphabet * (2 * (j - i + 1)):
                                        result.add(temp)
    return result