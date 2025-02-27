def palindromes_between_indices(s):
    range_str = s[0:6]
    english_letters = [c for c in range_str if c.isalpha() and c.isascii()]
    if len(set(english_letters)) < 5:
        return set()
    else:
        return {p for p in set((''.join(p) for p in permutations(english_letters, len(set(english_letters))))) if p == ''.join(reversed(p)) and len(p) >= 5}