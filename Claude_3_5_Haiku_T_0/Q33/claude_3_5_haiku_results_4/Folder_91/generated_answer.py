def return_vowels(string):
    vowels = 'aeiouAEIOU'
    result = [char for char in string[4:8] if char in vowels and 'P' < char <= 'r']
    return result