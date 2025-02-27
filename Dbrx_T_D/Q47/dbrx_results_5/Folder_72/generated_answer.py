def palindromes_of_specific_lengths(input_string):
    english_letters = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    palindromes = set()
    for length in range(27, 59):
        for index in range(26, len(input_string) - length + 1):
            substring = input_string[index:index + length].lower()
            if english_letters.issuperset(substring) and substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes