def palindromes_of_specific_lengths(s):
    palindromes = set()
    english_letters = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    for length in range(14, 53):
        for i in range(39, 95 - length + 1):
            if s[i:i + length].lower() == s[i:i + length].lower()[::-1] and english_letters.issuperset(s[i:i + length]):
                palindromes.add(s[i:i + length])
    return palindromes