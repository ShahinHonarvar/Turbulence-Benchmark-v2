def palindromes_of_specific_lengths(input_string):
    english_letters = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    palindromes = set()
    for i in range(23, 95):
        for length in range(17, 56):
            if i + length - 1 < 95:
                substring = input_string[i:i + length]
                if english_letters.issuperset(substring):
                    if substring.lower() == substring.lower()[::-1]:
                        palindromes.add(substring)
    return palindromes