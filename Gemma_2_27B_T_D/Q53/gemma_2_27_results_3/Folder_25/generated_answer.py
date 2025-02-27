def palindrome_of_length_at_least_n(text):
    return {s for s in text.lower().split() if len(s) >= 38 and s == s[::-1]}