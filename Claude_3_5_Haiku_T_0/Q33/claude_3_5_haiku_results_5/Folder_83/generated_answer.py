def return_vowels(string):
    vowels = 'aeiouAEIOU'
    result = [char for char in string[90:97] if char in vowels and '_' < char <= 'x']
    return result