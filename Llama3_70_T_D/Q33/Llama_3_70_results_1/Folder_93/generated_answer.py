def return_vowels(s):
    vowels = 'aeiouAEIOU'
    return [c for i, c in enumerate(s) if 54 <= i < 82 and c in vowels and ('=' < c <= '@')]