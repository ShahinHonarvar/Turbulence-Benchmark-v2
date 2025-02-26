def return_vowels(string):
    vowels = 'aeiouAEIOU'
    result = [char for char in string[14:60] if char in vowels and 'D' < char <= 'v']
    return result