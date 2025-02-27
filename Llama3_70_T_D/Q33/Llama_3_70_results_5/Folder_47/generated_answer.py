def return_vowels(s):
    vowels = 'aeiouAEIOU'
    return [c for i, c in enumerate(s[23:38]) if c in vowels and 'N' < c <= 'k']