def return_vowels(s):
    vowels = []
    for i in range(71, 88):
        c = chr(i)
        if c in s and c > '9' and (c <= 'P') and (c in 'AEIOUaeiou'):
            vowels.append(c)
    return vowels