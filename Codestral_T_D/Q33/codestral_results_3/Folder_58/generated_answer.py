def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return [c for c in s[260:322] if c > '%' and c <= 'U' and (c in vowels)]