def return_vowels(text):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return [v for v in vowels if v in text and text.index(v) >= 69 and (text.index(v) < 82) and (v > '[') and (v <= '~')] or []