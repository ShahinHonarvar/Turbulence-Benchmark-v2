def palindrome_of_length_n(text):
    text = text.lower()
    res = set()
    for i in range(len(text)):
        for j in range(i + 1, len(text)):
            if text[i:j] == text[j:i:-1]:
                res.add(text[i:j + 1])
    return res