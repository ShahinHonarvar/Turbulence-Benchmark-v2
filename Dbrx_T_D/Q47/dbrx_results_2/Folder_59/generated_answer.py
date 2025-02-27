def palindromes_of_specific_lengths(input_string):
    english_letters = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    palindromes = set()
    for length in range(3, 16):
        for index in range(100 - length + 1):
            substring = input_string[index:index + length]
            if set(substring) <= english_letters and substring == substring[::-1]:
                palindromes.add(substring.lower())
    return palindromes