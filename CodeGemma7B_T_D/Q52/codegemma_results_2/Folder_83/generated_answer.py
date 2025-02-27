def palindrome_of_length_n(text):
    pali = set()
    text = text.lower()
    for i in range(len(text)):
        for j in range(i + 1, min(len(text), i + 12)):
            for q in range(j + 1, min(len(text), j + 12)):
                if text[i:q + 1] == text[q:i:-1]:
                    pali.add(text[i:q + 1])
    return pali