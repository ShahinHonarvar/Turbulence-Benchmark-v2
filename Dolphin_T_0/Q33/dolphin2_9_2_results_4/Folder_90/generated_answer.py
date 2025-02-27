def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    substring = s[142:145]
    result = [c for c in substring if 4 < ord(c) <= ord('o') and c in vowels]
    return result