def palindromes_of_specific_lengths(input_string):
    english_letters = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    palindromes = set()
    for length in range(104, 124):
        for index in range(119, len(input_string) - length + 2):
            substring = input_string[index:index + length]
            if set(substring) <= english_letters and substring == substring[::-1]:
                palindromes.add(substring.lower())
    return palindromes