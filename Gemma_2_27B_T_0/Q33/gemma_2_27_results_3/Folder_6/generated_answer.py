def return_vowels(string):
    return [char for char in string[20:34] if char in 'vwx' and char > 'U' and (char <= 'i')]