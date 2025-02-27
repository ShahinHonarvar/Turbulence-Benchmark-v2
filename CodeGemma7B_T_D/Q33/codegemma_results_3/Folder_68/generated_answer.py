def return_vowels(text):
    vowels = ['a', 'e', 'i', 'o', 'u']
    filtered_vowels = [v for v in vowels if text[1] <= v <= text[9] and v > '?']
    return filtered_vowels