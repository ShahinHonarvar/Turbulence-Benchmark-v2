def return_vowels(string):
    vowels = 'aeiouAEIOU'
    result = [char for char in string[495:837] if char in vowels and 'B' < char <= 't']
    return result