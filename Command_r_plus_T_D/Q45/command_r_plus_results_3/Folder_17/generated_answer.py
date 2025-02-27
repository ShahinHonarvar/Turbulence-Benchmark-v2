def palindromes_between_indices(s: str) -> set:
    english_letters = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    s_letters = set(s[2:7])
    palindromes = set()
    for letter in s_letters:
        if letter in english_letters:
            s_letters.remove(letter)
            s_letters.remove(letter.lower())
            s_letters.add(letter)
    for letter in s_letters:
        if len(s_letters) >= 2:
            for other_letter in s_letters:
                if letter != other_letter:
                    palindrome = letter + other_letter + other_letter + letter
                    palindromes.add(palindrome)
    return palindromes