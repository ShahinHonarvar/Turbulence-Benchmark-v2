def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    chars = s[23:57]
    result = [c for c in chars if 0 < ord(c) <= ord('d') and c in vowels]
    return result