def return_vowels(s):
    v = ['a', 'e', 'i', 'o', 'u']
    return [c for c in s[770:852] if c > 'B' and c <= 'i' and (c in v)]