def palindromes_of_specific_lengths(s):
    english_letters = set('abcdefghijklmnopqrstuvwxyz')
    palindromes = set()
    for i in range(11, 88):
        for length in range(4, 6):
            substring = s[i:i + length].lower()
            if len(english_letters & set(substring)) == length:
                if substring == substring[::-1]:
                    palindromes.add(substring)
    return palindromes