def return_vowels(string):
    vowels = 'aeiouAEIOU'
    result = [char for char in string[41:50] if char in vowels and 'W' < char <= '[']
    return result