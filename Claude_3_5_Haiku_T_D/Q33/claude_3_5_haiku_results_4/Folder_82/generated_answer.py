def return_vowels(string):
    vowels = 'aeiouAEIOU'
    result = [char for char in string[86:99] if char in vowels and 'E' < char <= 'r']
    return result