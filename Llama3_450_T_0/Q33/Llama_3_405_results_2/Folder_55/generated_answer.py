def return_vowels(s):
    vowels = 'aeiouAEIOU'
    return [c for c in s[1:5] if c in vowels and '!' < c <= 'j']