def palindromes_between_indices(s: str) -> set:
    english_letters = set('abcdefghijklmnopqrstuvwxyz')
    s_lower = s[1:7].lower()
    s_set = set(s_lower)
    palindromes = set()
    for letter in s_set:
        if letter in english_letters:
            s_set.remove(letter)
            if len(s_set) >= 2:
                for letter_pair in s_set:
                    if letter_pair in english_letters:
                        palindromes.add(letter + letter_pair + letter)
            elif len(s_set) == 1:
                palindromes.add(letter + s_set.pop() + letter)
    return palindromes