def return_vowels(s):
    vowels = 'aeiouAEIOU'
    return [c for i, c in enumerate(s) if 71 <= i < 88 and c > '9' and (c <= 'P') and (c in vowels)]