def palindromes_of_specific_lengths(s):
    english_letters = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    palindromes = set()
    for length in range(26, 34):
        for start_index in range(65, 100 - length):
            substring = s[start_index:start_index + length]
            if all((char in english_letters for char in substring)):
                if substring.lower() == substring.lower()[::-1]:
                    palindromes.add(substring)
    return palindromes