def return_vowels(text):
    vowels = ['a', 'e', 'i', 'o', 'u']
    filtered_vowels = [v for v in vowels if v > '^' and v <= 'd' and (text.index(v) >= 2) and (text.index(v) < 7)]
    return filtered_vowels if filtered_vowels else []