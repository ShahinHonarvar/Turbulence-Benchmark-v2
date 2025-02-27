def return_vowels(s):
    vowels = 'aeiouAEIOU'
    return [c for c in s[14:60] if c in vowels and 'D' < c <= 'v']