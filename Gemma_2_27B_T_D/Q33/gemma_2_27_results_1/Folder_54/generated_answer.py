def return_vowels(string):
    return [char for char in string[23:85] if char in 'aeiouAEIOU' and char > 'W' and (char <= 'v')]