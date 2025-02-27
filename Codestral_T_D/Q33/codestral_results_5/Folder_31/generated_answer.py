def return_vowels(string):
    vowels = ['A', 'E', 'I', 'O', 'U']
    return [char for char in string[65:70] if char in vowels and '%' < char <= 'G']