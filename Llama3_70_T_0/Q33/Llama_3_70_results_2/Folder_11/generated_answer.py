def return_vowels(s):
    vowels = 'aeiouAEIOU'
    return [c for i, c in enumerate(s) if 29 <= i < 73 and c in vowels and ('#' < c <= '.')]