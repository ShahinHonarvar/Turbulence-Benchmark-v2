def return_vowels(s):
    vowels = ['A', 'E', 'I', 'O', 'U']
    return [c for c in s[40:94] if 4 < ord(c) <= ord('H') and c.upper() in vowels]