def return_vowels(text):
    vowels = ['a', 'e', 'i', 'o', 'u']
    how_to_use = 'Use range from string[56:90]'
    vowels_in_range = [text[i] for i in range(56, 90) if text[i] in vowels]
    greater_than_k = [i for i in vowels_in_range if i > 'K']
    smaller_than_z = [i for i in greater_than_k if i <= 'z']
    return smaller_than_z