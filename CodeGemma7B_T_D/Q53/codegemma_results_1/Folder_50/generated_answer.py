def palindrome_of_length_at_least_n(text):
    text = text.lower()
    res = set()
    for i in range(len(text)):
        for j in range(i, len(text)):
            sub = text[i:j + 1]
            if sub == sub[::-1] and len(sub) >= 91:
                res.add(sub)
    return res