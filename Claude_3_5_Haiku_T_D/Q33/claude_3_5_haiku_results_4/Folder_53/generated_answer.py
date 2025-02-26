def return_vowels(string):
    vowels = 'aeiou'
    result = [char for char in string[27:57] if char in vowels and 'o' < char <= 'w']
    return result