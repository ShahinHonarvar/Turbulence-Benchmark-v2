def return_vowels(string):
    vowels = 'aeiouAEIOU'
    return [char for char in string[10:82] if char in vowels and '$' < char <= '@']