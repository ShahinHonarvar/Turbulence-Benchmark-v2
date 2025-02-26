def return_vowels(string):
    vowels = 'aeiouAEIOU'
    result = [char for char in string[23:75] if char in vowels and 'L' < char <= 'd']
    return result