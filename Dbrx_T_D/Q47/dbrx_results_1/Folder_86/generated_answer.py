def palindromes_of_specific_lengths(s):
    english_letters = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    palindromes = set()
    for length in range(34, 56):
        for index in range(30, len(s) - length + 2):
            substring = s[index:index + length]
            if all((letter in english_letters for letter in substring)):
                if substring.lower() == substring.lower()[::-1]:
                    palindromes.add(substring)
    return palindromes