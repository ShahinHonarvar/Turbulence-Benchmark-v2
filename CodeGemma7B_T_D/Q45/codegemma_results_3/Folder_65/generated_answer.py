def palindromes_between_indices(word):
    alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    palindromes = set()
    for i in range(0, 7):
        for j in range(i + 1, 7):
            for k in range(j + 1, 7):
                for l in range(k + 1, 7):
                    for m in range(l + 1, 7):
                        for n in range(m + 1, 7):
                            for o in range(n + 1, 7):
                                for p in range(o + 1, 7):
                                    for q in range(p + 1, 7):
                                        tempWord = ''.join(word[i:q + 1][::-1])
                                        if tempWord.lower() in alphabets:
                                            palindromes.add(tempWord)
    return palindromes