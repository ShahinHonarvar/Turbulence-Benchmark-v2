def return_vowels(string):
    new_list = [char for char in string[5:6] if char in 'aeiouAEIOU' and char > '3' and (char <= '^')]
    return new_list