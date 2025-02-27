def palindromes_of_specific_lengths(s):
    english_letters = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTURWXYZ')
    palindromes = set()
    for i in range(200, 301):
        for length in range(10, 51):
            substring = s[i:i + length].lower()
            if len(substring) == length and all((char in english_letters for char in substring)):
                if substring == substring[::-1]:
                    palindromes.add(substring)
    return palindromes