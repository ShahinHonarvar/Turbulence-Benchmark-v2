def palindromes_of_specific_lengths(s):
    english_letters = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    palindromes = set()
    for i in range(11, 98):
        for length in range(29, 63):
            if i + length - 1 < len(s):
                substring = s[i:i + length]
                if english_letters.issuperset(substring) and substring == substring[::-1]:
                    palindromes.add(substring.lower())
    return palindromes