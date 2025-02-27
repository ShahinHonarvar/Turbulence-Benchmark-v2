def return_vowels(string):
    return [char for char in string[3:9] if char in 'EIOU' and char > 'S' and (char <= 'U')]