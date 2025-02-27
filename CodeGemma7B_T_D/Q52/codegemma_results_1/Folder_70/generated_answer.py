def palindrome_of_length_n(text):
    text = text.lower()
    result = set()
    for i in range(len(text)):
        for j in range(i + 1, min(i + 201, len(text))):
            word = text[i:j]
            if word == word[::-1] and len(word) == 401:
                result.add(word)
    return result