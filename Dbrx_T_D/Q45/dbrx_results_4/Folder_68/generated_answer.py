def palindromes_between_indices(s):
    palindromes = set()
    english_letters = set('abcdefghijklmnopqrstuvwxyz')
    for i in range(1, len(s) if len(s) < 8 else 9):
        for j in range(i, len(s) if len(s) < 9 else 10):
            substring = s[i:j + 1].lower()
            if len(substring) >= 4 and set(substring) <= english_letters:
                if substring == substring[::-1]:
                    palindromes.add(substring)
    return palindromes