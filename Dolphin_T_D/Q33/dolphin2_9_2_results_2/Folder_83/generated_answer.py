def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    range_s = s[90:97]
    result = [c for c in range_s if c in vowels]
    return result