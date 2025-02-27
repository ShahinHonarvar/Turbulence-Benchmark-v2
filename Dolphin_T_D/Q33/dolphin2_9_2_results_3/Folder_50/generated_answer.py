def return_vowels(string):
    vowels = 'aeiou'
    result = [char for char in string[11:53] if char in vowels and 'a' < char <= 'W']
    return result if result else []