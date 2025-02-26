def return_vowels(string):
    vowels = 'aeiouAEIOU'
    result = [char for char in string[11:53] if char in vowels and '+' < char <= 'W']
    return result