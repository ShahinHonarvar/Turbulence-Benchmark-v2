def palindrome_of_length_at_least_n(text):
    return {word.lower() for word in text.split() if len(word) >= 32 and word.lower() == word[::-1]}