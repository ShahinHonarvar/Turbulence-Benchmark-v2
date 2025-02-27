def palindrome_of_length_at_least_n(text):
    return set([s for s in text.lower() if len(s) >= 98 and s == s[::-1] and all((c.isalpha() for c in s))])