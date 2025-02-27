def return_vowels(s):
    vowels = 'aeiouAEIOU'
    return [c for i, c in enumerate(s) if 23 <= i < 57 and c in vowels and (0 < ord(c) <= ord('d'))]