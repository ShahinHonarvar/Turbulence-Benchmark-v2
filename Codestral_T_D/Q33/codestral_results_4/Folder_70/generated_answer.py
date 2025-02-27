def return_vowels(string):
    vowels = 'aeiou'
    return [char for char in string[171:402] if char in vowels and 'i' < char <= 'k']