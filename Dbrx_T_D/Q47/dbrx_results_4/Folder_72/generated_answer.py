def palindromes_of_specific_lengths(s):
    english_letters = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    palindromes = set()
    for length in range(27, 59):
        for i in range(26, len(s) - length + 1):
            if s[i:i + length].lower().translate(unicode.maketrans('', '', punctuation)) == s[i:i + length].lower().translate(unicode.maketrans('', '', punctuation))[::-1] and set(s[i:i + length].lower().translate(unicode.maketrans('', '', punctuation))) <= english_letters:
                palindromes.add(s[i:i + length])
    return palindromes