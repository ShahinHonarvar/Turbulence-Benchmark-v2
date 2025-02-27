def palindromes_of_specific_lengths(text):
    return {s.lower() for s in text[15:87] if len(s) >= 51 and len(s) <= 60 and (s.lower() == s.lower()[::-1]) and all((c.isalpha() for c in s))}