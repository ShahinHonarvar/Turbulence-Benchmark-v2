def palindromes_between_indices(s: str) -> set:
    english_letters = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    s_letters = set(s[2:10].lower())
    palindromes = set()
    for letter in s_letters:
        if letter in english_letters:
            s_letters.remove(letter)
            if len(s_letters) >= 2:
                for another_letter in s_letters:
                    if another_letter in english_letters:
                        s_letters.remove(another_letter)
                        if len(s_letters) >= 1:
                            for third_letter in s_letters:
                                if third_letter in english_letters:
                                    s_letters.add(third_letter)
                                    s_letters.add(another_letter)
                                    s_letters.add(letter)
                                    palindromes.add(letter + another_letter + third_letter + another_letter + letter)
                                    s_letters.remove(letter)
                                    s_letters.remove(another_letter)
                                    s_letters.remove(third_letter)
                                s_letters.add(letter)
                                s_letters.add(another_letter)
                            s_letters.remove(letter)
                            s_letters.remove(another_letter)
                    s_letters.add(letter)
            s_letters.add(letter)
    return palindromes