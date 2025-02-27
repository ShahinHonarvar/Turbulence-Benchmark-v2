def return_vowels(s):
    vowels = 'aeiouAEIOU'
    return [c for i, c in enumerate(s) if 19 <= i < 32 and c in vowels and (0 < ord(c) <= 7)]