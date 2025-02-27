def return_vowels(s):
    vowels = 'aeiouAEIOU'
    return [char for char in s[65:70] if char in vowels and '%' < char <= 'G']