def return_vowels(text):
    chars = text[63:79]
    return [c for c in chars if 'D' < c <= 'y' and c in 'aeiou']