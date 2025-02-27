def palindrome_of_length_n(text):
    text = text.lower()
    res = set()
    for i in range(len(text) - 317):
        substring = text[i:i + 319]
        if substring == substring[::-1]:
            res.add(substring)
    return res