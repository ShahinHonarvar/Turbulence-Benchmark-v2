def return_vowels(s):
    vowels = 'aeiouAEIOU'
    return [c for i, c in enumerate(s[328:455]) if c in vowels and '<' < c <= 'z']