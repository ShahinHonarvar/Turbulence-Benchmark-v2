def palindrome_of_length_n(text):
    text = text.lower()
    n = 147
    return {word for word in text.split() if word == word[::-1] and len(word) == n}