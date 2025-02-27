def palindrome_of_length_n(text):
    return set([t for t in text.lower().split() if len(t) == 147 and t == t[::-1]])