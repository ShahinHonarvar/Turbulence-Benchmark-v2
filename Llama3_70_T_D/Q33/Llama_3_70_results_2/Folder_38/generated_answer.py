def return_vowels(s):
    vowels = [c for i, c in enumerate(s) if 17 <= i < 65 and 'U' < c <= '{' and (c in 'AEIOUaeiou')]
    return vowels