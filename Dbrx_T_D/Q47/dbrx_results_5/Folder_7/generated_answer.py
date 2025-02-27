def palindromes_of_specific_lengths(s):
    english_letters = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    palindromes = set()
    for length in range(104, 124):
        for i in range(119, 257 - length + 1):
            if s[i:i + length].lower().encode('ascii').islower() and s[i:i + length].lower().encode('ascii').isalpha():
                if all((letter in english_letters for letter in s[i:i + length].lower())):
                    if s[i:i + length].lower() == s[i:i + length].lower()[::-1]:
                        palindromes.add(s[i:i + length].lower())
    return palindromes