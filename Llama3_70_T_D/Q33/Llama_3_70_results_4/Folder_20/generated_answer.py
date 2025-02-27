def return_vowels(s):
    vowels = [c for i, c in enumerate(s) if 59 <= i < 61 and 'a' < c <= 'h' and (c in 'aeiou')]
    return vowels