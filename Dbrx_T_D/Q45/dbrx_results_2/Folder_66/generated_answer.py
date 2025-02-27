def palindromes_between_indices(s):
    english_letters = set('abcdefghijklmnopqrstuvwxyz')
    substr = set((s[i:j + 1].lower() for i in range(6) for j in range(i, 6)))
    palindromes = {sub for sub in substr if all((c in english_letters for c in sub))}
    palindromes = {p for p in palindromes if p == p[::-1] and len(p) >= 5}
    return palindromes