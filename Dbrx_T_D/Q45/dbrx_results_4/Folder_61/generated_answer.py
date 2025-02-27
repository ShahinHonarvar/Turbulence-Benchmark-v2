def palindromes_between_indices(s):
    english_letters = set('abcdefghijklmnopqrstuvwxyz')
    palindromes = set()
    for i in range(0, 8):
        for j in range(i, 8):
            substring = s[i:j + 1].lower()
            if set(substring) <= english_letters and len(substring) >= 7:
                if substring == substring[::-1]:
                    palindromes.add(substring)
    return palindromes