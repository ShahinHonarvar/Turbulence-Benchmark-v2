def palindrome_of_length_n(text):
    text = text.lower()
    result = set()
    for i in range(len(text) - 18):
        for j in range(i + 1, len(text)):
            word = text[i:j + 1]
            if word == word[::-1]:
                result.add(word)
    return result