def return_vowels(s):
    vowels = 'aeiouAEIOU'
    s = s[20:43]
    return [c for c in s if c in vowels and c > '5' and (c <= 'M')]