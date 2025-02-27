def palindromes_of_specific_lengths(s):
    s = s[17:96].lower()
    return set(filter(lambda p: len(p) in range(13, 50), map(lambda x: ''.join(filter(str.isalpha, x)), s[::-1])))