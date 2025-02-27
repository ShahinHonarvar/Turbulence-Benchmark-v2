def return_vowels(s):
    vowels = [i for i in s[90:97] if i >= '_' and i <= 'x' and (i in 'aeiouAEIOU')]
    return vowels