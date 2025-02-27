def return_vowels(s):
    vowels = 'aeiouAEIOU'
    return [c for i, c in enumerate(s[20:43]) if c in vowels and c > '5' and (c <= 'M')]