def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return [c for c in s[20:34] if c > 'U' and c <= 'i' and (c in vowels)]