def return_vowels(s):
    vowels = 'aeiouAEIOU'
    return [c for c in s[23:57] if 0 < ord(c) <= ord('d') and c in vowels]