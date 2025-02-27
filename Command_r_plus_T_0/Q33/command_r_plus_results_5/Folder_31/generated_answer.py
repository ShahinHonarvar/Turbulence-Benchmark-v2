def return_vowels(s):
    vowels = ['A', 'E', 'I', 'O', 'U']
    result = [v for v in s[65:70] if v.upper() in vowels and v >= '%' and (v <= 'G')]
    return result