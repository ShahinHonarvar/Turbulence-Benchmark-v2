def return_vowels(string):
    vowels = 'aeiouAEIOU'
    result = [char for char in string[149:313] if char in vowels and 'M' < char <= 'j']
    return result