def return_vowels(s):
    vowels = [c for i, c in enumerate(s) if 20 <= i < 41 and c > 'K' and (c <= 'Z') and (c in 'AEIOU')]
    return vowels