def palindromes_between_indices(s: str) -> set:
    english_letters = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    s_letters = set(s[6:10])
    palindromes = set()
    for letter in s_letters:
        if letter in english_letters:
            s_letters.remove(letter)
            s_letters.add(letter.lower())
    for letter in s_letters:
        if letter in english_letters:
            s_letters.remove(letter)
            s_letters.add(letter.upper())
    for p in s_letters:
        if len(p) >= 5 and p == p[::-1]:
            palindromes.add(p)
    return palindromes