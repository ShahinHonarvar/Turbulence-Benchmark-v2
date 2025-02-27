def return_vowels(s):
    vowels = 'aeiouAEIOU'
    return [c for i, c in enumerate(s[70:76], start=70) if c in vowels and c > chr(2) and (c <= chr(58))]