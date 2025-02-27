def return_vowels(s):
    vowels = 'aeiouAEIOU'
    return [c for i, c in enumerate(s[63:79], start=63) if c in vowels and c > 'D' and (c <= 'y')]