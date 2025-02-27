def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return [char for char in string[65:70] if char in vowels and '%' < char <= 'G']