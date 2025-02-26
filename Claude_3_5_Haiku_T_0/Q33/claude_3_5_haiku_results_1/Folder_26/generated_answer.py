def return_vowels(string):
    vowels = 'aeiouAEIOU'
    result = [char for char in string[10:82] if char in vowels and '$' < char <= '@']
    return result