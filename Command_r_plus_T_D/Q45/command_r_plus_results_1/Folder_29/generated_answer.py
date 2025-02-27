def palindromes_between_indices(s: str) -> set:
    s = s[2:10]
    english_letters = set('abcdefghijklmnopqrstuvwxyz')
    s_letters = set(s.lower())
    palindromes = set()
    for letter in s_letters:
        if letter in english_letters:
            count = s.count(letter)
            if count >= 3:
                palindromes.add(letter * count)
    return palindromes