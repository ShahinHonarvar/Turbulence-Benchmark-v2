def palindrome_of_length_at_least_n(text):
    return {word for word in text.lower().split() if word == word[::-1] and len(word) >= 10}