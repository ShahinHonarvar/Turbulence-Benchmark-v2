def return_vowels(s):
    vowels = 'aeiouAEIOU'
    return [c for i, c in enumerate(s) if 24 <= i < 64 and c > 'F' and (c <= 'h') and (c in vowels)]