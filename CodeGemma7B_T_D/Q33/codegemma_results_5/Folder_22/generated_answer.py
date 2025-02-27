def return_vowels(text):
    return [x for x in text[56:90].lower() if x in ['a', 'e', 'i', 'o', 'u'] and x > 'k' and (x <= 'z')]