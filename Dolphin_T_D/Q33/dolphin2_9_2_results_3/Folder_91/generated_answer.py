def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = [c for c in s[4:8] if c > 'p' and c <= 'r' and (c in vowels)]
    return result