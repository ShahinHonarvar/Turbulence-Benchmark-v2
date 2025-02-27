def palindromes_between_indices(s):
    english_letters = 'abcdefghijklmnopqrstuvwxyz'
    english_letters += english_letters.upper()
    s = s.lower()
    pallindromes = set()
    for i in range(2, 10):
        for j in range(i, 10):
            substring = s[i:j + 1]
            if all((letter in english_letters for letter in substring)):
                if substring == substring[::-1]:
                    pallindromes.add(substring)
    return pallindromes