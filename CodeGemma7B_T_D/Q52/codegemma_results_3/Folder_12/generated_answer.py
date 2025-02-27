def palindrome_of_length_n(text):
    text = text.lower()
    text = ''.join(filter(str.isalpha, text))
    result = set()
    for i in range(len(text) - 23):
        for j in range(i + 23, len(text)):
            if text[i:j + 1] == text[j:j - i - 1:-1]:
                result.add(text[i:j + 1])
    return result