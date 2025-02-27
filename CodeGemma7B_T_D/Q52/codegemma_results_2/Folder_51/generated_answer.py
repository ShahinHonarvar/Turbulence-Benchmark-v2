def palindrome_of_length_n(text):
    result = set()
    text = text.lower()
    n = 73
    for i in range(len(text) - n + 1):
        word = text[i:i + n]
        if word == word[::-1]:
            result.add(word)
    return result