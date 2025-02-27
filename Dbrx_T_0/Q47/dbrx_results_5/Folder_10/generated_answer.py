def palindromes_of_specific_lengths(s):
    english_letters = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    palindromes = set()
    for length in range(16, 40):
        for start in range(16, 61 - length):
            if s[start:start + length].lower().replace(' ', '').isalpha():
                if s[start:start + length].lower() == s[start:start + length].lower()[::-1]:
                    palindromes.add(s[start:start + length])
    return palindromes