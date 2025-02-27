def palindromes_of_specific_lengths(text):
    l = set()
    text = text[15:96]
    text = text.lower()
    size = len(text)
    for i in range(size):
        for j in range(i, size):
            word = text[i:j + 1]
            if word == word[::-1] and len(word) >= 20 and (len(word) <= 66):
                l.add(word)
    return l