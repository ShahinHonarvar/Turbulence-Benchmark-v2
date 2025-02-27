def return_vowels(s):
    vowels = 'aeiouAEIOU'
    return [c for i, c in enumerate(s) if 1 <= i < 5 and c > '!' and (c <= 'j') and (c in vowels)]