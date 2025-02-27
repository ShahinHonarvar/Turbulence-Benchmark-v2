def return_vowels(s):
    vowels = 'aeiouAEIOU'
    return [c for c in s[328:455] if c in vowels and '<' < c <= 'z']