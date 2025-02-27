def palindromes_of_specific_lengths(text):
    result = set()
    text = text.lower()
    for i in range(20):
        for j in range(4, 81):
            for x in range(i, i + j):
                if x + j > len(text):
                    break
                y = text[x:x + j]
                if y == y[::-1]:
                    result.add(y)
    return result