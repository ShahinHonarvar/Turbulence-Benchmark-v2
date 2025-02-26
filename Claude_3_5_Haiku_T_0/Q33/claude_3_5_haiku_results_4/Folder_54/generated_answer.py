def return_vowels(string):
    vowels = 'aeiouAEIOU'
    result = [char for char in string[23:85] if char in vowels and 'W' < char <= 'v']
    return result