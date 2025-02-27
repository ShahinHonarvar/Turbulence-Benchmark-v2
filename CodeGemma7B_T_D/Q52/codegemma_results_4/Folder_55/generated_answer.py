def palindrome_of_length_n(text):
    result = set()
    text = text.lower()
    for i in range(len(text) - 97 + 1):
        for j in range(i + 97, len(text) + 1):
            if text[i:j] == text[j - 1:i - 1:-1]:
                result.add(text[i:j])
    return result