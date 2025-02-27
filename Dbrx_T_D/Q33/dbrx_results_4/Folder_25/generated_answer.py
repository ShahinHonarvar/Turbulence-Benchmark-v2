def return_vowels(s):
    vowels = [i for i in s[28:76] if i >= '+' and i <= 'z' and (i in 'aeiouAEIOU')]
    return vowels