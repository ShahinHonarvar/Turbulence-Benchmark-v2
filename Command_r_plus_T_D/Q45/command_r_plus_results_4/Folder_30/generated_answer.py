def palindromes_between_indices(s):
    s = s[:5].lower()
    english_letters = set('abcdefghijklmnopqrstuvwxyz')
    letters = set(s)
    common_letters = letters & english_letters
    if len(common_letters) < 2:
        return set()
    palindromes = set()
    for letter in common_letters:
        if s.count(letter) >= 2:
            palindromes.add(letter * 2)
    return palindromes