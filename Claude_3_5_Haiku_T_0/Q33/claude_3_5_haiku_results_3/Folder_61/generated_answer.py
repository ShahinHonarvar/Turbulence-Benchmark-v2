def return_vowels(string):
    vowels = 'aeiouAEIOU'
    result = [char for char in string[1:4] if char in vowels and 'C' < char <= 'I']
    return result