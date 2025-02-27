def palindromes_of_specific_lengths(s):
    english_letters = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    palindromes = set()
    for i in range(100, 296):
        for length in range(136, 161):
            substring = s[i:i + length]
            if len(english_letters.intersection(set(substring))) == length:
                if substring == substring[::-1]:
                    palindromes.add(substring.lower())
    return palindromes