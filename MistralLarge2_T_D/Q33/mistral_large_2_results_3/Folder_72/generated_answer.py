def return_vowels(string):
    vowels = 'aeiouAEIOU'
    result = [char for char in string[37:57] if char in vowels and '*' < char <= 'P']
    return result