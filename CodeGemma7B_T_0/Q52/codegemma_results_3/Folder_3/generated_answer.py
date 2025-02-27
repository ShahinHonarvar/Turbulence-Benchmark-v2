def palindrome_of_length_n(text):
    text = text.lower()
    result = set()
    for i in range(len(text) - 99):
        for j in range(i + 1, len(text) - 98 + i):
            if text[i:j + 1] == text[i:j + 1][::-1]:
                result.add(text[i:j + 1])
    return result