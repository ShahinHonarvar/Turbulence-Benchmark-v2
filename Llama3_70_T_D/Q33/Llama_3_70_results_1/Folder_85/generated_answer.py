def return_vowels(s):
    vowels = 'aeiouAEIOU'
    return [c for i, c in enumerate(s) if 55 <= i < 65 and c in vowels and ('Z' < c <= 'w')]