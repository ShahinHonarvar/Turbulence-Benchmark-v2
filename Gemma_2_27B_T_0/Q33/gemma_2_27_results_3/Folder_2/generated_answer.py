def return_vowels(string):
    return [char for char in string[170:645] if char in 'Iiou' and char <= '~' and (char > 'E')]