def return_vowels(s):
    v = ['a', 'e', 'i', 'o', 'u']
    return [c for c in s[85:99] if c in v and '\\' < c <= 'n']