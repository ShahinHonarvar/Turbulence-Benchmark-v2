def return_vowels(string):
    vowels = 'aeiouAEIOU'
    result = [char for char in string[64:82] if char in vowels and 'P' < char <= 'z']
    return result