def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return [c for c in s[3:9] if c > 'S' and c <= 'U' and (c in vowels)]