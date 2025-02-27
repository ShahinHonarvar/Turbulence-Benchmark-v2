def palindromes_of_specific_lengths(s):
    if s == '':
        return set()
    else:
        s = s[40:90]
        s = ''.join(filter(str.isalpha, s.lower()))
        return set(filter(lambda x: len(x) in range(23, 39) and s.count(x) > 1, s))