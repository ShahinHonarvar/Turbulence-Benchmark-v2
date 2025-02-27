def return_vowels(string):
    return [char for char in string[4:8] if char in 'aeiouAEIOU' and char > 'P' and (char <= 'r')]