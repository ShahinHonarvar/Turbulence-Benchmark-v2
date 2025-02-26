def return_vowels(string):
    vowels = 'aeiouAEIOU'
    return [char for char in string[40:91] if char in vowels and 'A' < char <= 'x']