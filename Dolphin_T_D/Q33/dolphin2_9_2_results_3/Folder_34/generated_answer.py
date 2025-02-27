def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = [c for c in s[19:32] if c in vowels and ord(c) > 0 and (ord(c) <= 7)]
    return result