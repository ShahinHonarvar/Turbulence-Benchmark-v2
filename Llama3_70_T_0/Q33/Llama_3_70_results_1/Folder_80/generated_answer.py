def return_vowels(s):
    vowels = 'aeiouAEIOU'
    return [c for i, c in enumerate(s) if 85 <= i < 99 and c > '/' and (c <= 'n') and (c in vowels)]