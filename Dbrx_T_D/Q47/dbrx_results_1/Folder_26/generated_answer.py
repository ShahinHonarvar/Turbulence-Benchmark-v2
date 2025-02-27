def palindromes_of_specific_lengths(string):
    english_letters = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    palindromes = set()
    for i in range(24, 85):
        for j in range(21, 32):
            if i + j - 1 <= min(84, len(string)):
                substring = string[i - 1:i + j - 1]
                if all((letter in english_letters for letter in substring)):
                    if substring == substring[::-1]:
                        palindromes.add(substring)
    return palindromes