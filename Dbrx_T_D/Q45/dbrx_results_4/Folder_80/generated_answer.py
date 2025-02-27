def palindromes_between_indices(given_string):
    english_letters = set('abcdefghijklmnopqrstuvwxyz')
    palindromes = set()
    for i in range(3, 9):
        for j in range(i, 9):
            substring = given_string[i:j + 1].lower()
            if set(substring).issubset(english_letters):
                if len(substring) >= 7 and substring == substring[::-1]:
                    palindromes.add(substring)
    return palindromes