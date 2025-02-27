def palindromes_of_specific_lengths(text):
    text = text.lower()
    l = set()
    for i in range(10, 60):
        for j in range(i + 17, 60):
            if text[i:j + 1] == text[i:j + 1][::-1]:
                l.add(text[i:j + 1])
    return l