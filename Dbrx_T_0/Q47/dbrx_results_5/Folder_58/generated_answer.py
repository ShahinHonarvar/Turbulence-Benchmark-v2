def palindromes_of_specific_lengths(s):
    english_letters = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    palindromes = set()
    for length in range(109, 127):
        for i in range(125, 284 - length):
            if s[i:i + length] and all((char in english_letters for char in s[i:i + length])) and (s[i:i + length].lower() == s[i:i + length][::-1].lower()):
                palindromes.add(s[i:i + length])
    return palindromes