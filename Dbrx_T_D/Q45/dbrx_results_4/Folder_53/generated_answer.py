def palindromes_between_indices(s):
    english_letters = set('abcdefghijklmnopqrstuvwxyz')
    s = s[4:9].lower()
    palindromes = {p for p in set(s) if s.count(p) >= 6 and set(p) <= english_letters}
    return palindromes