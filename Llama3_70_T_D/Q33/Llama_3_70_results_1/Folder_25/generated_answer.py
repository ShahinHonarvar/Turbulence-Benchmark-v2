def return_vowels(s):
    vowels = 'aeiouAEIOU'
    return [c for c in s[28:76] if c in vowels and '+' < c <= 'z']