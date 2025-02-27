def return_vowels(text):
    text = text.lower()
    list_vowels_specifieds = []
    for x in [text[3:8]]:
        for y in x:
            if y in ['a', 'e', 'i', 'o', 'u'] and y > ';' and (y <= 'd'):
                list_vowels_specifieds.append(y)
    if not list_vowels_specifieds:
        return list_vowels_specifieds
    return list_vowels_specifieds