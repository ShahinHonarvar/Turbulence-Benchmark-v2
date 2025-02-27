def return_vowels(s):
    vowels = 'aeiouAEIOU'
    result = [c for c in s[40:94] if c in vowels and c > '4' and (c <= 'H')]
    return result