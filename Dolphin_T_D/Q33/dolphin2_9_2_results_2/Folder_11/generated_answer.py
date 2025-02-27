def return_vowels(string):
    vowels = 'aeiou'
    return [char for char in string[29:73] if string[6].__lt__(char).__lt__(string[7]) and char in vowels]