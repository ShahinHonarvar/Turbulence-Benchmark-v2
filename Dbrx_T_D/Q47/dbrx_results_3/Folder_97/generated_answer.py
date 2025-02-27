def palindromes_of_specific_lengths(input_string):
    english_letters = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    palindromes = set()
    for i in range(28, 95):
        for j in range(38, 50):
            if i + j - 1 <= 94:
                substring = input_string[i:i + j]
                if substring.lower().translate({ord(c): None for c in english_letters}) == '':
                    if substring == substring[::-1]:
                        palindromes.add(substring)
    return palindromes