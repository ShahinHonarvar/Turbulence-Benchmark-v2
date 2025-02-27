def palindromes_of_specific_lengths(text):
    lower = text.lower()
    pals = set()
    poss = []
    for i in range(33, 86):
        poss.append(i)
        poss.append(i - 1)
    for i in poss:
        for j in range(i, i - 31, -1):
            if j not in poss:
                continue
            tmp = lower[j:i + 1]
            if tmp == tmp[::-1]:
                pals.add(tmp)
    return pals