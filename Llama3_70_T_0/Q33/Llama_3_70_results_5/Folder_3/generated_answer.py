def return_vowels(s):
    vowels = 'aeiouAEIOU'
    return [c for i, c in enumerate(s) if 50 <= i < 77 and c in vowels and ('#' < c <= 'r')]