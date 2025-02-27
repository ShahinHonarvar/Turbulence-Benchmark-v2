def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return [c for c in s[27:57] if c > 'o' and c <= 'w' and (c in vowels)]