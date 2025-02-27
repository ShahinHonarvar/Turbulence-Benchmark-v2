def palindromes_of_specific_lengths(s):
    english_letters = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    palindromes = set()
    for length in range(39, 53):
        for start_index in range(16, 95 - length + 1):
            substring = s[start_index:start_index + length]
            if all((char in english_letters for char in substring)):
                if substring == ''.join(reversed(substring)):
                    palindromes.add(substring)
    return palindromes