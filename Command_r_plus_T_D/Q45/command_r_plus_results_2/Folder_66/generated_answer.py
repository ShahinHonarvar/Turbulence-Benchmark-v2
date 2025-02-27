def palindromes_between_indices(s):
    s = s.lower()
    english_letters = set('abcdefghijklmnopqrstuvwxyz')
    letters_in_range = set((s[i] for i in range(6) if s[i] in english_letters))
    palindromes = set()
    for p in letters_in_range:
        if p * 5 in s.lower()[:6]:
            palindromes.add(p * 5)
    return palindromes