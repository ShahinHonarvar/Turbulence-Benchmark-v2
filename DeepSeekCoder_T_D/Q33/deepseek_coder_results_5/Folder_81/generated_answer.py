def return_vowels(s):
    vowels = 'aeiouAEIOU'
    result = [c for c in s[20:43] if c in vowels and c > '5' and (c <= 'M')]
    return result