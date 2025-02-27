def return_vowels(string):
    return [char for char in string[149:313] if char in 'aeiouAEIOU' and char > 'M' and (char <= 'j')]