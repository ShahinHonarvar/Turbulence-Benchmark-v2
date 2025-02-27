def return_vowels(s):
    vowels = 'aeiouAEIOU'
    return [c for i, c in enumerate(s) if 40 <= i < 94 and c > chr(4) and (c <= 'H') and (c in vowels)]