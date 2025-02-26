def return_vowels(string):
    vowels = 'aeiouAEIOU'
    return [char for char in string[23:75] if char in vowels and 'L' < char <= 'd']