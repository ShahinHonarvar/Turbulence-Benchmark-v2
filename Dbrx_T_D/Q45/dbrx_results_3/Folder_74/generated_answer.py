def palindromes_between_indices(s):
    english_letters = set('abcdefghijklmnopqrstuvwxyz')
    palindromes = set()
    for i in range(1, 7):
        for j in range(i, 7):
            substring = s[i:j + 1].lower()
            if english_letters.issuperset(substring):
                if substring == substring[::-1]:
                    palindromes.add(substring)
    return palindromes