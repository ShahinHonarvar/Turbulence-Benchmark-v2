def return_vowels(s):
    vowels = 'aeiouAEIOU'
    return [c for i, c in enumerate(s[23:57]) if c in vowels and '0' < c <= 'd']