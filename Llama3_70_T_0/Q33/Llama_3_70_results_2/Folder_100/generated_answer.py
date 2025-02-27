def return_vowels(s):
    vowels = 'aeiouAEIOU'
    return [c for c in s[23:75] if c in vowels and 'L' < c <= 'd']