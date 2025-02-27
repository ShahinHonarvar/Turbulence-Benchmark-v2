def palindrome_of_length_n(text):
    text = text.lower()
    result = set()
    for i in range(len(text) - 38 + 1):
        for j in range(i + 38, len(text) + 1):
            if text[i:j] == text[i:j][::-1]:
                result.add(text[i:j])
    return result