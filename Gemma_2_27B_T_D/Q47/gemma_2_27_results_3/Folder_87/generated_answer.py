def palindromes_of_specific_lengths(text):
    return {s for s in set(text[11:94]) if s.isalpha() and len(s) in range(34, 55) and (s.lower() == s[::-1].lower())}