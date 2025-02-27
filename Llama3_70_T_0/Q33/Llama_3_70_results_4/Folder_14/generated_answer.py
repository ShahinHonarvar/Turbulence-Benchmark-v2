def return_vowels(s):
    vowels = 'aeiouAEIOU'
    return [c for i, c in enumerate(s) if 47 <= i < 61 and c > '\\    ' and (c <= 'O') and (c in vowels)]