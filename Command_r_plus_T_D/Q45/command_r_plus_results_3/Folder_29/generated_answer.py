def palindromes_between_indices(s: str) -> set:
    english_letters = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    s_letters = set(s[2:10].lower())
    palindromes = set()
    for letter in s_letters:
        if letter in english_letters:
            s_letters.remove(letter)
            break
    for letter in s_letters:
        if letter in english_letters:
            s_letters.remove(letter)
            break
    for letter in s_letters:
        if letter in english_letters:
            s_letters.remove(letter)
            break
    if len(s_letters) >= 3:
        for p in s_letters:
            palindromes.add(p + p[::-1])
    return palindromes