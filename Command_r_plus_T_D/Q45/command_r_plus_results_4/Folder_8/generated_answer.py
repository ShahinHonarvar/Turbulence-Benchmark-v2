def palindromes_between_indices(s):

    def is_palindrome(s):
        return s == s[::-1]
    english_letters = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    letters_between_indices = set(s[1:6])
    letters_between_indices = letters_between_indices.intersection(english_letters)
    palindromes = set()
    for p in letters_between_indices:
        if s.count(p) >= 5:
            palindromes.add(p * 5)
        for q in letters_between_indices:
            if s.count(p) + s.count(q) >= 5:
                palindromes.add(p * (5 - s.count(q)) + q * s.count(q))
            for r in letters_between_indices:
                if s.count(p) + s.count(q) + s.count(r) >= 5:
                    palindromes.add(p * (5 - s.count(q) - s.count(r)) + q * s.count(q) + r * s.count(r))
                    palindromes.add(p * (5 - s.count(q) - s.count(r)) + q * s.count(r) + r * s.count(q))
                for t in letters_between_indices:
                    if s.count(p) + s.count(q) + s.count(r) + s.count(t) >= 5:
                        palindromes.add(p * (5 - s.count(q) - s.count(r) - s.count(t)) + q * s.count(q) + r * s.count(r) + t * s.count(t))
                        palindromes.add(p * (5 - s.count(q) - s.count(r) - s.count(t)) + q * s.count(r) + r * s.count(q) + t * s.count(t))
                        palindromes.add(p * (5 - s.count(q) - s.count(r) - s.count(t)) + q * s.count(r) + r * s.count(t) + t * s.count(q))
                        palindromes.add(p * (5 - s.count(q) - s.count(r) - s.count(t)) + q * s.count(t) + r * s.count(q) + t * s.count(r))
    palindromes = set((p for p in palindromes if is_palindrome(p)))
    return palindromes