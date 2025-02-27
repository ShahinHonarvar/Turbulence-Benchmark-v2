def return_vowels(string):
    return [char for char in string[90:97] if char in 'aeiouAEIOU' and '_' < char <= 'x']