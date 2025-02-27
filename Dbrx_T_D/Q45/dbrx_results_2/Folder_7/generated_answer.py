def palindromes_between_indices(s):
    english_letters = set('abcdefghijklmnopqrstuvwxyz')
    palindromes = set()
    for i in range(1, 10):
        for j in range(i, 10):
            substring = s[i - 1:j].lower()
            if len(substring) >= 7 and set(substring).issubset(english_letters):
                if substring == substring[::-1]:
                    palindromes.add(substring)
    return palindromes