def palindromes_of_specific_lengths(s):
    english_letters = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    palindromes = set()
    for length in range(14, 40):
        for i in range(34, 91 - length):
            if s[i:i + length].lower().translate(str.maketrans('', '', '0123456789')) == s[i:i + length].lower().translate(str.maketrans('', '', '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~')):
                if all((char in english_letters for char in s[i:i + length])):
                    palindromes.add(s[i:i + length])
                    break
    return palindromes