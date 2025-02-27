def return_vowels(s):
    vowels = [c for c in s[170:645] if 'E' < c <= '~' and c in 'AEIOUaeiou']
    return vowels