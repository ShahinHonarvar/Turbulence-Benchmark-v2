def return_vowels(s):
    vowels = [c for c in s if 90 <= ord(c) < 97 and '_' < c <= 'x' and (c in 'aeiouAEIOU')]
    return vowels