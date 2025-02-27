def palindromes_of_specific_lengths(s):
    english_letters = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    palindromes = set()
    for length in range(52, 57):
        for i in range(26, len(s) - length + 1):
            if s[i:i + length].lower().translate(str.maketrans('', '', '0123456789')) in palindromes:
                continue
            if all((char in english_letters for char in s[i:i + length])):
                palindromes.add(s[i:i + length].lower().translate(str.maketrans('', '', '0123456789')))
    return palindromes