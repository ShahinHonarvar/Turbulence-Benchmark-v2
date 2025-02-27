def return_vowels(string):
    return [char for char in string[55:65] if char in 'aeiouAEIOU' and char > 'Z' and (char <= 'w')]