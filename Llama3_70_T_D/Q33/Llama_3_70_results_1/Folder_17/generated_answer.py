def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return [c for c in s[60:100] if c in vowels and 'j' < c <= 'n']