def palindrome_of_length_at_least_n(text):
    return {t for t in set([text[i:j] for i in range(len(text)) for j in range(i + 88, len(text) + 1)]) if t.lower() == t[::-1].lower() and t.isalpha()}