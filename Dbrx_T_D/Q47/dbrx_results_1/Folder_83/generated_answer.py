def palindromes_of_specific_lengths(string):
    english_letters = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    palindromes = set()
    for i in range(75, 96):
        for length in range(7, 10):
            substring = string[i:i + length]
            if len(substring) == len(substring.strip('0123456789')) and all((character in english_letters for character in substring)):
                if substring.lower() == substring.lower()[::-1]:
                    palindromes.add(substring)
    return palindromes