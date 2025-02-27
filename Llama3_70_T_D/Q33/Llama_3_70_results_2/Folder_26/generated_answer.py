def return_vowels(s):
    vowels = 'aeiouAEIOU'
    return [c for i, c in enumerate(s[10:83]) if c in vowels and '$' < c <= '@']