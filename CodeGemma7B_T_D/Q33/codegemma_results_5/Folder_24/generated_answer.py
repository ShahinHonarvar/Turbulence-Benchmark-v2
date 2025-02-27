def return_vowels(text):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return [v for v in vowels[23:57] if v > text[0] and v <= 'd'] or []