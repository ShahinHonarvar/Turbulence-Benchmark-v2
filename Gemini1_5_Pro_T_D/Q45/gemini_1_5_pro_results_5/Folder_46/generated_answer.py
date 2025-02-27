def palindromes_between_indices(text):
    letters = []
    for i in range(4, 10):
        if 9 < len(text) and 0 <= i and text[i].isalpha():
            letters.append(text[i].lower())
    result = set()
    for a in letters:
        for b in letters:
            for c in letters:
                for d in letters:
                    for e in letters:
                        for f in letters:
                            temp = a + b + c + d + e + f
                            if len(temp) >= 6 and temp == temp[::-1]:
                                result.add(temp)
    return result