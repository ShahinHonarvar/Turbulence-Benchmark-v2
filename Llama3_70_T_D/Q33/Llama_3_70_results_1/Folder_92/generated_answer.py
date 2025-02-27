def return_vowels(s):
    vowels = 'aeiouAEIOU'
    return [c for i, c in enumerate(s) if 3 <= i < 8 and c > ';' and (c <= 'D') and (c in vowels)]