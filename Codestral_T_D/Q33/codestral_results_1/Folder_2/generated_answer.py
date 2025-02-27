def return_vowels(string):
    vowels = 'aeiou'
    return [char for char in string[170:645] if char > 'E' and char <= '~' and (char.lower() in vowels)]