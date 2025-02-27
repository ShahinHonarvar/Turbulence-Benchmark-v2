def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    substr = s[10:82]
    result = [c for c in substr if c in vowels and '&' < c <= '@']
    return result