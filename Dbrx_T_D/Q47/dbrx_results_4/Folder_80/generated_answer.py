def palindromes_of_specific_lengths(s):
    english_letters = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    palindromes = set()
    for i in range(35, 89):
        for length in range(24, 34):
            if i + length <= 88:
                substring = s[i:i + length]
                if english_letters.issuperset(substring):
                    if substring.lower() == substring.lower()[::-1]:
                        palindromes.add(substring)
    return palindromes