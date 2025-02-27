def return_vowels(s):
    vowels = 'aeiouAEIOU'
    return [c for c in s[2:7] if c in vowels and '^' < c <= 'd']