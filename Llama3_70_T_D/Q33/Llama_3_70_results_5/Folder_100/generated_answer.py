def return_vowels(s):
    vowels = 'aeiouAEIOU'
    s = s[23:75]
    return [c for c in s if c in vowels and 'L' < c <= 'd']