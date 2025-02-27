def palindrome_of_length_n(text):
    text = text.lower()
    result = set()
    for i in range(len(text) - 18):
        for j in range(i + 19):
            if text[i:j] == text[j - 1:i - 1:-1]:
                result.add(text[i:j])
    return result