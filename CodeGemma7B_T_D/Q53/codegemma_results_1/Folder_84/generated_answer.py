def palindrome_of_length_at_least_n(text):
    res, w = (set(), 0)
    for i, c in enumerate(text.lower()):
        for j in range(26):
            if i - j - 1 >= w and text.lower()[i - j - 1:i + j + 1] == text.lower()[i - j - 1:i + j + 1][::-1]:
                res.add(text[i - j - 1:i + j + 1])
                w = i - j - 1
    return res