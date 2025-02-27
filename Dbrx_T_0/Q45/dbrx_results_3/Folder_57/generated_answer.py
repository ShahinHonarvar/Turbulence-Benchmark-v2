def palindromes_between_indices(s):
    english_letters = set('abcdefghijklmnopqrstuvwxyz')
    palindromes = set()
    for i in range(2, 6):
        for j in range(i, 6):
            substring = s[i:j + 1].lower()
            if set(substring).issubset(english_letters):
                if len(substring) >= 5 and substring == substring[::-1]:
                    palindromes.add(substring)
    return palindromes