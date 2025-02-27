def return_vowels(s):
    vowels = 'aeiouAEIOU'
    return [c for i, c in enumerate(s) if 51 <= i < 77 and c in vowels and (c > chr(4)) and (c <= chr(61))]