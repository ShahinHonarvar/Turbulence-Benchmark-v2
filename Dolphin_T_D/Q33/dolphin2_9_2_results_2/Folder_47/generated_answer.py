def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = [c for c in s[23:38] if c > 'N' and c <= 'k' and (c in vowels)]
    return result