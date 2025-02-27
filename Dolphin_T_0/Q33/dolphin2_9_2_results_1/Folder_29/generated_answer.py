def return_vowels(s):
    v = ['a', 'e', 'i', 'o', 'u']
    output = [c for c in s[19:20] if c in v and '<' < c <= 'p']
    return output