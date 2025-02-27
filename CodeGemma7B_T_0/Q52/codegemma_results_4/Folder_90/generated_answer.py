def palindrome_of_length_n(text):
    text = text.lower()
    result = set()
    for i in range(len(text) - 317):
        for j in range(i + 1, len(text) - 316):
            for k in range(j + 1, len(text) - 315):
                if text[i:j + 1] == text[k:j + 1][::-1]:
                    result.add(text[i:j + 1])
    return result