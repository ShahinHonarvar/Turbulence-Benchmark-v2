def palindromes_between_indices(s: str) -> set:
    palindromes = set()
    english_letters = set('abcdefghijklmnopqrstuvwxyz')
    s_lower = s[2:9].lower()
    for letter in s_lower:
        if letter in english_letters:
            english_letters.remove(letter)
    if len(english_letters) >= 3:
        for letter in english_letters:
            palindromes.add(s_lower[1:3] + letter + s_lower[1:3][::-1])
    return palindromes