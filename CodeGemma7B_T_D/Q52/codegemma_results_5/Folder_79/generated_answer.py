def palindrome_of_length_n(string):
    return {word for word in string.lower().split() if word == word[::-1] and len(word) == 64}