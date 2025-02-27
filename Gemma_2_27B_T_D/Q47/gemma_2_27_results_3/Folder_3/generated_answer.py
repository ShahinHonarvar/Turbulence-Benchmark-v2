def palindromes_of_specific_lengths(text):
    return {p for p in set(text[27:96]) if 49 <= len(p) <= 51 and p.isalpha() and (p.lower() == p[::-1].lower())}