def return_vowels(s):
    vowels = 'aeiouAEIOU'
    return [char for char in s[10:82] if char in vowels and '$' < char <= '@']