def palindromes_of_specific_lengths(s):
    english_letters = set('abcdefghijklmnopqrstuvwxyz')
    palindromes = set()
    for i in range(6):
        for j in range(i + 3, i + 6):
            if j <= len(s):
                substring = s[i:j].lower()
                if english_letters.issuperset(substring) and substring == substring[::-1]:
                    palindromes.add(substring)
    return palindromes