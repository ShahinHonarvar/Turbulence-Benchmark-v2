def return_vowels(string):
    vowels = 'aeiou'
    result = [char for char in string[60:99] if char.lower() in vowels and 'j' < char.lower() <= 'n']
    return result