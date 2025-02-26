def return_vowels(string):
    vowels = 'aeiouAEIOU'
    result = [char for char in string[24:64] if char in vowels and 'F' < char <= 'h']
    return result