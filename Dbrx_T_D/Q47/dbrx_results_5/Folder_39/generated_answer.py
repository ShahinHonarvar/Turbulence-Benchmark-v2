def palindromes_of_specific_lengths(s):
    english_letters = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    palindromes = set()
    for length in range(50, 54):
        for i in range(31, 92 - length):
            if all((c in english_letters for c in s[i:i + length])):
                if s[i:i + length] == s[i:i + length][::-1]:
                    palindromes.add(s[i:i + length].lower())
    return palindromes