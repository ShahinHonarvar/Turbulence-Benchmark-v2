def return_vowels(string):
    vowels = 'aeiouAEIOU'
    result = [char for char in string[28:76] if char in vowels and '+' < char <= 'z']
    return result