def palindromes_between_indices(s):
    english_letters = set('abcdefghijklmnopqrstuvwxyz')
    palindromes = set()
    for i in range(1, 8):
        for j in range(i, 8):
            substring = s[i - 1:j].lower()
            if english_letters.issuperset(substring):
                if substring == substring[::-1] and len(substring) >= 3:
                    palindromes.add(substring)
    return palindromes