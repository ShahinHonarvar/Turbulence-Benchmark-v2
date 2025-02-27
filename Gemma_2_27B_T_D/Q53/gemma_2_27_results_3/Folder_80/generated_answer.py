def palindrome_of_length_at_least_n(text):
    return {t for t in set(''.join(filter(str.isalpha, text)).lower().split()) if len(t) >= 30 and t == t[::-1]}