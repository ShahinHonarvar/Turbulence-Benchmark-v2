def return_vowels(string):
    vowels = 'aeiouAEIOU'
    result = [char for char in string[21:23] if char in vowels and '-' < char <= 'n']
    return result