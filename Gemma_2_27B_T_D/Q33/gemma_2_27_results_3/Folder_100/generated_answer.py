def return_vowels(string):
    return [char for char in string[23:75] if char in 'aeiouAEIOU' and char > 'L' and (char <= 'd')]