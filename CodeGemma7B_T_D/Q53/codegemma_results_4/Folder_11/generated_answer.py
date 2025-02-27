def palindrome_of_length_at_least_n(text):
    res = set()
    for start in range(54):
        for end in range(start + 54, len(text) + 1):
            if text[start:end].lower() == text[start:end][::-1].lower():
                res.add(text[start:end].lower())
    return res