def palindromes_of_specific_lengths(s):
    english_letters = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    palindromes = set()
    for length in range(37, 61):
        for start in range(11, 84 - length + 1):
            if s[start:start + length].lower() == s[start:start + length][::-1].lower() and all((char in english_letters for char in s[start:start + length])):
                palindromes.add(s[start:start + length])
    return palindromes