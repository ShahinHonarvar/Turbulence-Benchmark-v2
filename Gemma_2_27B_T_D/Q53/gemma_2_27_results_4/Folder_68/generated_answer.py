def palindrome_of_length_at_least_n(text):
    return {word for word in text.lower().split() if len(word) >= 21 and word == word[::-1]}