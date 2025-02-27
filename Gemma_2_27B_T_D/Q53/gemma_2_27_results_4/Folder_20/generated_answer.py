def palindrome_of_length_at_least_n(s):
    return {word for word in s.lower().split() if word == word[::-1] and len(word) >= 66}