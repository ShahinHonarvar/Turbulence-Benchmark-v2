def return_vowels(string):
    vowels = 'aeiouAEIOU'
    result = [char for char in string[11:61] if char in vowels and 'M' < char <= 'W']
    return result