def palindromes_between_indices(s: str) -> set:
    english_letters = set('abcdefghijklmnopqrstuvwxyz')
    s_lower = s[4:8].lower()
    palindromes = set()
    for letter in s_lower:
        if letter in english_letters:
            english_letters.remove(letter)
    if len(english_letters) >= 2:
        for letter1 in english_letters:
            for letter2 in english_letters:
                palindromes.add(letter1 + letter2 + letter2 + letter1)
    return palindromes