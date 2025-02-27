def palindromes_between_indices(s):
    english_letters = set('abcdefghijklmnopqrstuvwxyz')
    substr = ''.join((c.lower() for c in s[5:8] if c.lower() in english_letters))
    palindromes = {p for n in range(3, len(substr) + 1) for p in {substr[i:n + i] for i in range(len(substr) - n + 1)} if p == p[::-1]}
    return palindromes