def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return [c for c in s[71:81] if c in vowels and '>' < c <= 'U']