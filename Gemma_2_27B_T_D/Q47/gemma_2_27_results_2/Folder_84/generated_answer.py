def palindromes_of_specific_lengths(text):
    sub_text = text[23:78]
    return {p for p in set([s for s in sub_text if s.isalpha() and s.lower() == s.lower()[::-1]]) if 13 <= len(p) <= 40}