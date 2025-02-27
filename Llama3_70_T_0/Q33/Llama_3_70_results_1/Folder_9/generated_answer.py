def return_vowels(s):
    vowels = 'aeiouAEIOU'
    return [c for i, c in enumerate(s) if 13 <= i < 35 and c in vowels and (ord(c) > 8) and (ord(c) <= ord('F'))]