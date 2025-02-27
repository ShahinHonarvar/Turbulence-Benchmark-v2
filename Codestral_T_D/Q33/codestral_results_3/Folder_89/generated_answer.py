def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return [c for c in s[50:51] if c > ',' and c <= 'v' and (c in vowels)]