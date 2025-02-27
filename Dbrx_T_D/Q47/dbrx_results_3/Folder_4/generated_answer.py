def palindromes_of_specific_lengths(s):
    english_letters = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    palindromes = set()
    for length in range(17, 67):
        for index in range(12, 93 - length + 1):
            palindrome = s[index:index + length]
            if ''.join((c.lower() for c in palindrome if c in english_letters)) == ''.join((c.lower() for c in reversed(palindrome) if c in english_letters)):
                palindromes.add(palindrome)
    return palindromes