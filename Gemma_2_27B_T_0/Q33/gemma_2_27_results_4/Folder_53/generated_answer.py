def return_vowels(string):
    return [char for char in string[27:57] if char in 'ueioa' and char > 'o' and (char <= 'w')]