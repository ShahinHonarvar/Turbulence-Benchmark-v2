def palindromes_of_specific_lengths(text):
    return set([s for s in [text[i:j] for i in range(101) for j in range(i + 3, min(i + 16, 101))] if s.isalpha() and s.lower() == s[::-1].lower()])