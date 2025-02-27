def palindromes_of_specific_lengths(s):
    english_letters = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    palindromes = set()
    for i in range(15, 90):
        for length in range(40, 73):
            if i + length <= 90:
                substring = s[i:i + length]
                if substring.lower().count(substring[0].lower()) == len(substring) and set(substring).issubset(english_letters):
                    if substring == substring[::-1]:
                        palindromes.add(substring)
    return palindromes