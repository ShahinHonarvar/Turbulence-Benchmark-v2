def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = [c for c in s[10:83] if c > '%' and c <= 'e' and (c in vowels)]
    return result