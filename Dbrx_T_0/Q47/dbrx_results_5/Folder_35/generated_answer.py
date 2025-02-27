def palindromes_of_specific_lengths(s):
    english_letters = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    palindromes = set()
    for length in range(14, 40):
        for start in range(34, 91 - length):
            if s[start:start + length].lower().isalpha() and all((char in english_letters for char in s[start:start + length])):
                if s[start:start + length].lower() == s[start:start + length][::-1].lower():
                    palindromes.add(s[start:start + length])
    return palindromes