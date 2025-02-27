def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    range_chars = s[1:4]
    result = [c for c in range_chars if c in vowels and 'c' < c <= 'i']
    return result