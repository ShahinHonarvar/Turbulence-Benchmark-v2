def return_vowels(s):
    vowels = []
    for i in range(46, 49):
        try:
            c = s[i]
            if c > '[' and c <= 'p' and (c in 'aeiouAEIOU'):
                vowels.append(c)
        except IndexError:
            break
    return vowels