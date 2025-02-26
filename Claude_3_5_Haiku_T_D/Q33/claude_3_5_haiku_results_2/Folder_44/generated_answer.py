def return_vowels(string):
    vowels = 'aeiouAEIOU'
    result = [char for char in string[46:49] if char in vowels and '[' < char <= 'p']
    return result