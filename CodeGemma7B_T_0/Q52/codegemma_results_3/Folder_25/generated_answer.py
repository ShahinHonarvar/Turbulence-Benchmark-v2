def palindrome_of_length_n(text):
    text = text.lower()
    result = set()
    for i in range(len(text) - 89):
        for j in range(i + 1, len(text) - 89 + i + 1):
            if text[i:j] == text[j:i:-1]:
                result.add(text[i:j])
    return result