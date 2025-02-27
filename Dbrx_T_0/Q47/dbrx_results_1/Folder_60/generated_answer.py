def palindromes_of_specific_lengths(s):
    english_letters = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    palindromes = set()
    for i in range(23, 83):
        for length in range(32, 35):
            if i + length <= 82:
                substring = s[i:i + length]
                if substring.lower().count(substring[0].lower()) == len(substring) and set(substring).issubset(english_letters):
                    if substring == substring[::-1]:
                        palindromes.add(substring)
    return palindromes