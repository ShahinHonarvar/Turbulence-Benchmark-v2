def return_vowels(s):
    vowels = 'aeiouAEIOU'
    return [c for i, c in enumerate(s) if 11 <= i < 53 and c > '+' and (c <= 'W') and (c in vowels)]