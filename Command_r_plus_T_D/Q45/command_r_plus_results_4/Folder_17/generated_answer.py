def palindromes_between_indices(s: str) -> set:
    english_letters = set('abcdefghijklmnopqrstuvwxyz')
    s_letters = set(s[2:7].lower())
    palindromes = set()
    for letter in s_letters:
        if letter in english_letters:
            s_letters.remove(letter)
            if len(s_letters) >= 2:
                for second_letter in s_letters:
                    if second_letter in english_letters:
                        s_letters.remove(second_letter)
                        if len(s_letters) >= 1:
                            for third_letter in s_letters:
                                if third_letter in english_letters:
                                    palindromes.add(letter + second_letter + third_letter + second_letter + letter)
                        s_letters.add(third_letter)
                s_letters.add(second_letter)
            if len(s_letters) >= 1:
                for second_letter in s_letters:
                    if second_letter in english_letters:
                        palindromes.add(letter + second_letter + letter)
            s_letters.add(letter)
    return palindromes