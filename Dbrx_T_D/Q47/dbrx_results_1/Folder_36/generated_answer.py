def palindromes_of_specific_lengths(s):
    english_letters = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    palindromes = set()
    for length in range(115, 135):
        for index in range(124, 284 - length + 1):
            substring = s[index:index + length]
            if set(substring) <= english_letters and substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes