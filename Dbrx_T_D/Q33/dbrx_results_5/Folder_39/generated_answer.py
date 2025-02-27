def return_vowels(s):
    vowels = [c for c in s if 32 <= ord(c) < 97 and 'Q' < c <= ']' and (c in 'AEIOU')]
    return vowels