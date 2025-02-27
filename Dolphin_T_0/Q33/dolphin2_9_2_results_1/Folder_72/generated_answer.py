def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    range_s = s[37:57]
    result = [i for i in range_s if i in vowels and i > '*' and (i <= 'P')]
    return result