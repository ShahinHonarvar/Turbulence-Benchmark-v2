def return_vowels(s):
    vowels = 'aeiouAEIOU'
    return [c for i, c in enumerate(s) if 55 <= i < 65 and c > 'Z' and (c <= 'w') and (c in vowels)]