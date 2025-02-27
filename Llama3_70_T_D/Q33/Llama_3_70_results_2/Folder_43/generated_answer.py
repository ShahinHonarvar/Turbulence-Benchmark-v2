def return_vowels(s):
    vowels = [c for c in s[22:82] if c > 'N' and c <= 'o' and (c in 'AEIOUaeiou')]
    return vowels