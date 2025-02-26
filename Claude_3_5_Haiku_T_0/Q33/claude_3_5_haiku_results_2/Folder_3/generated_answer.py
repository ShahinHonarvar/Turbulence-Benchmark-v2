def return_vowels(string):
    vowels = 'aeiouAEIOU'
    result = [char for char in string[50:77] if char in vowels and '#' < char <= 'r']
    return result