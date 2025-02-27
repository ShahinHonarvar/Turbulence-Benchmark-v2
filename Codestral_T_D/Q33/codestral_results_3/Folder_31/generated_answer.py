def return_vowels(s):
    vowels = ['A', 'E', 'I', 'O', 'U']
    result = [char for char in s[65:70] if char in vowels and char > '%' and (char <= 'G')]
    return result