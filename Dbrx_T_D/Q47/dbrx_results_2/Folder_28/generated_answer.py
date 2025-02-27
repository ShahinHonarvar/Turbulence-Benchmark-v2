def palindromes_of_specific_lengths(s):
    english_letters = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    palindromes = set()
    for length in range(21, 33):
        for index in range(32, len(s) - length + 1):
            substring = s[index:index + length]
            if set(substring) <= english_letters and substring == substring[::-1]:
                palindromes.add(substring.lower())
    return palindromes