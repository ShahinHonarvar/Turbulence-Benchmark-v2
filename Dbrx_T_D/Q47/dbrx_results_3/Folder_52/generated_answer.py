def palindromes_of_specific_lengths(s):
    palindromes = set()
    english_letters = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    for length in range(13, 43):
        for start in range(44, 100 - length + 1):
            substring = s[start:start + length]
            if english_letters.issuperset(substring):
                if substring == ''.join(reversed(substring)):
                    palindromes.add(substring.lower())
    return palindromes