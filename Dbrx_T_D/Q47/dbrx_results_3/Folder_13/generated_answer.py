def palindromes_of_specific_lengths(s):
    english_letters = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    palindromes = set()
    for i in range(13, 96):
        for length in range(57, 61):
            if i + length - 1 < len(s) and all((c in english_letters for c in s[i:i + length])) and (s[i:i + length].lower() == s[i:i + length][::-1].lower()):
                palindromes.add(s[i:i + length])
    return palindromes