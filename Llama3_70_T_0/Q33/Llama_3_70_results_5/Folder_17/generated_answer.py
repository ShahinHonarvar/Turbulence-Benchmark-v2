def return_vowels(s):
    vowels = 'aeiouAEIOU'
    return [c for i, c in enumerate(s) if 60 <= i < 99 and c in vowels and ('j' < c <= 'n')]