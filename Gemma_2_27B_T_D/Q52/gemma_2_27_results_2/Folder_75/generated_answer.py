def palindrome_of_length_n(text):
    return set((x for x in [text[i:i + 80] for i in range(len(text) - 79)] if x.isalpha() and x.lower() == x[::-1].lower()))