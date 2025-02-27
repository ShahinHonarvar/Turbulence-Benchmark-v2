def palindromes_of_specific_lengths(text):
    return {t for t in set(text[29:99]) if t.isalpha() and t[::-1].lower() == t.lower() and (6 <= len(t) <= 9)}