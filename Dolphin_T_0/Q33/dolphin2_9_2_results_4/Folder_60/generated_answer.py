def return_vowels(txt):
    vowels = ['A', 'E', 'I', 'O', 'U']
    return [v for v in txt[24:59] if v in vowels and v > 'N' and (v <= 'U')]