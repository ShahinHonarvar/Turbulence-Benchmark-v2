def palindrome_of_length_at_least_n(text):
    lst = []
    text = text.lower()
    for q in range(len(text)):
        for w in range(q + 1, len(text)):
            for e in range(w + 1, len(text)):
                if text[q] == text[e] and text[w] == text[e]:
                    lst.append(text[q:e + 1])
    return set(lst)