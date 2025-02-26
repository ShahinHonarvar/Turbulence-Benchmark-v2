def return_vowels(string):
    vowels = 'aeiouAEIOU'
    result = [char for char in string[77:84] if char in vowels and '(' < char <= 'G']
    return result