def return_vowels(string):
    vowels = 'AEIOUaeiou'
    return [char for char in string[604:949] if char in vowels and 'N' < char <= 'U']