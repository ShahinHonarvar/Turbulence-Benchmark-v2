def palindromes_between_indices(input_string: str) -> set:
    palindromes = set()
    substring = input_string[7:10].lower()
    english_letters = set('abcdefghijklmnopqrstuvwxyz')
    substring_letters = set(substring)
    if substring_letters.issubset(english_letters):
        for letter in substring_letters:
            if substring.count(letter) >= 3:
                palindromes.add(letter * 3)
            elif substring.count(letter) == 2:
                for other_letter in substring_letters - {letter}:
                    if other_letter in substring:
                        palindromes.add(letter * 2 + other_letter)
    return palindromes