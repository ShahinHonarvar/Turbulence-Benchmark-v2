def return_vowels(s):
    vowels = 'aeiouAEIOU'
    return [c for i, c in enumerate(s) if 43 <= i < 70 and c > '*' and (c <= 'b') and (c in vowels)]