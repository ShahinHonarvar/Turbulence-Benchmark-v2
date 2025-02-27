def return_vowels(s):
    vowels = 'aeiouAEIOU'
    return [c for c in s[529:828] if c in vowels and 'U' < c <= 'l']