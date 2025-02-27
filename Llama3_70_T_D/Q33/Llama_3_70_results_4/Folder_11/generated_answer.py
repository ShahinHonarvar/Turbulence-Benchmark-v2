def return_vowels(s):
    vowels = [c for i, c in enumerate(s) if 29 <= i < 73 and '#' < c <= '.' and (c in 'aeiouAEIOU')]
    return vowels