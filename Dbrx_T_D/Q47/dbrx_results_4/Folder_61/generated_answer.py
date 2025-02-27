def palindromes_of_specific_lengths(string):
    english_letters = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    palindromes = set()
    for length in range(20, 31):
        for start_index in range(len(string) - length + 1):
            substring = string[start_index:start_index + length]
            if all((char in english_letters for char in substring)) and substring == substring[::-1]:
                palindromes.add(substring.lower())
    return palindromes