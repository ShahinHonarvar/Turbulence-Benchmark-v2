def return_vowels(text):
    vowels = ['a', 'e', 'i', 'o', 'u']
    filtered_vowels = [v for v in vowels if v in text[21:23] and v > '-' and (v <= 'n')]
    if not filtered_vowels:
        return []
    return filtered_vowels