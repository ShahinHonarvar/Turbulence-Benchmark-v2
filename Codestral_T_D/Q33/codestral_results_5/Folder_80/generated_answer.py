def return_vowels(string):
    vowels = 'aeiou'
    result = [char for char in string[85:99] if char.lower() in vowels and char > '/' and (char <= 'n')]
    return result