def return_vowels(s):
    l = ['E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '~']
    return [i for i in s[170:645] if i in l and i > l[0] and (i <= l[-1])]