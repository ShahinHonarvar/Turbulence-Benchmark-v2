def return_vowels(string):
    return [char for char in string[10:97] if char in 'aeiouAEIOU' and char > 'R' and (char <= 'b')]