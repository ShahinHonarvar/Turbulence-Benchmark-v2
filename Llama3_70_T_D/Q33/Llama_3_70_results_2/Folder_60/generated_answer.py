def return_vowels(s):
    vowels = [c for i, c in enumerate(s) if 24 <= i < 59 and 'N' < c <= 'U' and (c in 'AEIOUaeiou')]
    return vowels