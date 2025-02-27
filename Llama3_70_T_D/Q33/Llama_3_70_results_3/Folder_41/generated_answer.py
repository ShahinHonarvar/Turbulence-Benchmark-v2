def return_vowels(s):
    vowels = 'aeiouAEIOU'
    return [c for i, c in enumerate(s) if 71 <= i < 81 and c in vowels and ('>' < c <= 'U')]