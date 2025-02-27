def return_vowels(s):
    vowels = 'aeiouAEIOU'
    return [c for i, c in enumerate(s) if 5 <= i < 6 and c in vowels and (3 < ord(c) <= ord('^'))]