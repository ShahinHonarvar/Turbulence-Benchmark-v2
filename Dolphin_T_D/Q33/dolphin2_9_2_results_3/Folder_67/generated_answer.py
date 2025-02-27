def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = [c for c in s[21:59] if c in vowels and '\\' < c <= 'a']
    return result