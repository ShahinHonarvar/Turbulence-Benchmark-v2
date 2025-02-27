def palindromes_of_specific_lengths(s):
    english_letters = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    palindromes = set()
    for length in range(136, 161):
        for start in range(100, 296 - length):
            if s[start:start + length].lower().replace(' ', '').isalpha():
                if s[start:start + length].lower() == s[start:start + length][::-1].lower():
                    palindromes.add(s[start:start + length])
    return palindromes