def palindromes_of_specific_lengths(string):
    english_letters = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    palindromes = set()
    for length in range(119, 142):
        for index in range(127, 289 - length + 1):
            substring = string[index:index + length]
            if set(substring) <= english_letters and substring == substring[::-1]:
                palindromes.add(substring.lower())
    return palindromes