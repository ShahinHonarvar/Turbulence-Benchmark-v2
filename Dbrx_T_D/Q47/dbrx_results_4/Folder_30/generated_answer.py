def palindromes_of_specific_lengths(input_string):
    input_string = input_string[14:91]
    english_letters = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    palindromes = set()
    for i in range(len(input_string) - 54):
        for j in range(55, 72):
            substring = input_string[i:i + j]
            if english_letters.issuperset(substring):
                if substring == ''.join(reversed(substring)):
                    palindromes.add(substring)
    return palindromes