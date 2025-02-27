def return_vowels(s):
    vowels = 'aeiouAEIOU'
    return [c for c in s[495:837] if c in vowels and 'B' < c <= 't']