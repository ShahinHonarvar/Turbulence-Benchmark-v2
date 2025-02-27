def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return [c for c in s[328:455] if c > '<' and c <= 'z' and (c in vowels)]