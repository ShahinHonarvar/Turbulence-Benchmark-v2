def return_vowels(s):
    vowels = [c for i, c in enumerate(s) if 'F' < c <= 'h' and 24 <= i < 64 and (c in 'aeiou')]
    return vowels