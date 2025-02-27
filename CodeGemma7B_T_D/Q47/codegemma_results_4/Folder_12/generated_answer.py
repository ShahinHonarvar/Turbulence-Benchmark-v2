def palindromes_of_specific_lengths(text):
    cla, rla = (62, 88)
    low, high = (18, 21)
    result = set()
    for i in range(cla, rla + 1):
        for j in range(i - low, i - high - 1, -1):
            if not text[i].isalpha() or not text[j].isalpha():
                continue
            word = text[j:i + 1]
            if word == word[::-1]:
                result.add(word)
    return result