def return_vowels(string):
    vowels = 'aeiouAEIOU'
    return [char for char in string[3:9] if char in vowels and 'S' < char <= 'U']