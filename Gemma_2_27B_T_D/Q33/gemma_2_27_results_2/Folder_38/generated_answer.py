def return_vowels(string):
    return [char for char in string[17:65] if char in 'VWYZ' and char <= '{' and (char > 'U')]