def return_vowels(s):
    vowels = 'aeiouAEIOU'
    return [c for i, c in enumerate(s) if 21 <= i < 23 and c in vowels and ('-' < c <= 'n')]