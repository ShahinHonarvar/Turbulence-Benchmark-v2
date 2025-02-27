def return_vowels(text):
    vowels = ['a', 'e', 'i', 'o', 'u']
    filtered_vowels = [v for v in vowels[34:58] if v > 'b' and v <= 'o']
    return filtered_vowels or []