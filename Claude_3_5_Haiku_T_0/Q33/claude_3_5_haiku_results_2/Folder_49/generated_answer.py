def return_vowels(string):
    vowels = 'aeiouAEIOU'
    result = [char for char in string[10:97] if char in vowels and 'R' < char <= 'b']
    return result