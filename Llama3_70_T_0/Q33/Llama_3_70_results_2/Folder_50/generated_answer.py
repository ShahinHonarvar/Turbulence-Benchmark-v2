def return_vowels(s):
    vowels = 'aeiouAEIOU'
    return [c for c in s[11:53] if c in vowels and '+' < c <= 'W']