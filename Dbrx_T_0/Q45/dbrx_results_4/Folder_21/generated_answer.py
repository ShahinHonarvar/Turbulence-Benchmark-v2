def palindromes_between_indices(s):
    english_letters = set('abcdefghijklmnopqrstuvwxyz')
    palindromes = set()
    for i in range(1, 9):
        for j in range(i, 9):
            substring = s[i - 1:j].lower()
            if set(substring).issubset(english_letters):
                if len(substring) >= 7 and substring == substring[::-1]:
                    palindromes.add(substring)
    return palindromes