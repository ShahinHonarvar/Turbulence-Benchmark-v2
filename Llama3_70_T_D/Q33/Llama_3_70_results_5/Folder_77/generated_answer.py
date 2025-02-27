def return_vowels(string):
    vowels = 'AEIOUaeiou'
    return [char for char in string[837:975] if char in vowels and char > 'N' and (char <= 'W')]