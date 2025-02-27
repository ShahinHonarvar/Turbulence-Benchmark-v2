def return_vowels(string):
    vowels = 'aeiouAEIOU'
    return [char for char in string[2:7] if char in vowels and '^' < char <= 'd']