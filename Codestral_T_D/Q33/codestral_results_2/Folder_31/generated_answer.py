def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return [c for c in s[65:70] if c in vowels and c > '%' and (c <= 'G')]