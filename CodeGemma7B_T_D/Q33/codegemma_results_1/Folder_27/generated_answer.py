def return_vowels(text):
    return [ch for ch in text[29:31] if ch.lower() in ['a', 'e', 'i', 'o', 'u'] and 'a' < ch.lower() <= 'f']