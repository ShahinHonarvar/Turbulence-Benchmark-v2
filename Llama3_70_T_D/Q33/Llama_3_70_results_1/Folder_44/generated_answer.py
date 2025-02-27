def return_vowels(s):
    vowels = [s[i] for i in range(46, 49) if s[i] > '[' and s[i] <= 'p' and (s[i] in 'aeiou')]
    return vowels