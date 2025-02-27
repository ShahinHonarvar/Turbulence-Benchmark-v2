def palindromes_between_indices(s: str) -> set:
    english_letters = set('abcdefghijklmnopqrstuvwxyz')
    s_lower = s[3:8].lower()
    s_lower_set = set(s_lower)
    palindromes = set()
    for letter in s_lower:
        if letter in english_letters:
            s_lower_set.remove(letter)
            if len(s_lower_set) >= 2:
                for letter_pair in s_lower_set:
                    palindromes.add(letter + letter_pair + letter)
    return palindromes