def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    filtered_vowels = [v for v in vowels[1:7] if v > 'F' and v <= 'j']
    return filtered_vowels if filtered_vowels else []