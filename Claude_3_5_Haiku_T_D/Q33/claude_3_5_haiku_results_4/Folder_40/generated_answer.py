def return_vowels(string):
    vowels = 'aeiouAEIOU'
    result = [char for char in string[2:7] if char in vowels and '^' < char <= 'd']
    return result