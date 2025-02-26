def return_vowels(string):
    vowels = 'aeiouAEIOU'
    result = [char for char in string[20:43] if char in vowels and '5' < char <= 'M']
    return result