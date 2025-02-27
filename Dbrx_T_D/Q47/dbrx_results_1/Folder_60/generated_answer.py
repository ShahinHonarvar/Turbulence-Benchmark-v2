def palindromes_of_specific_lengths(s):
    english_letters = set('abcdefghijklmnopqrstuvwxyz')
    palindromes = set()
    for i in range(23, 83):
        for length in range(32, 35):
            substring = s[i:i + length].lower()
            if all((letter in english_letters for letter in substring)):
                if substring == substring[::-1]:
                    palindromes.add(substring)
    return palindromes