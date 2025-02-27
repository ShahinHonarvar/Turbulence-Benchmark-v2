def palindromes_of_specific_lengths(s):
    result = set()
    english_letters = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    for i in range(75, 96):
        for length in range(7, 10):
            substring = s[i:i + length]
            if len(substring) == len(set(substring).intersection(english_letters)) == length:
                if substring == substring[::-1]:
                    result.add(substring)
    return result