def palindrome_of_length_n(text):
    text = text.lower()
    result = set()
    for i in range(len(text) - 2):
        for j in range(i + 1, len(text) - 1):
            for k in range(j + 1, len(text)):
                if text[i] == text[k] and text[i + 1] == text[k - 1] and (text[i + 2] == text[k - 2]):
                    result.add(text[i:k + 1])
    return result