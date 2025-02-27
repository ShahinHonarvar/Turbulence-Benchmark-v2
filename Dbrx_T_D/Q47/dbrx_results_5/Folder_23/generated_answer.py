def palindromes_of_specific_lengths(input_string):
    english_letters = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    palindromes = set()
    for length in range(17, 56):
        for index in range(23, len(input_string) - length + 2):
            substring = input_string[index:index + length].lower()
            if english_letters.issuperset(substring):
                if substring == substring[::-1]:
                    palindromes.add(substring)
    return palindromes