def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    s = s[46:49]
    result = [c for c in s if c in vowels and 'a' <= c <= 'p']
    return result