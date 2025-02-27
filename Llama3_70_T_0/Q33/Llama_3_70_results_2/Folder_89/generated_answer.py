def return_vowels(s):
    vowels = 'aeiouAEIOU'
    return [c for i, c in enumerate(s) if 50 <= i < 51 and c in vowels and (c > ',') and (c <= 'v')]