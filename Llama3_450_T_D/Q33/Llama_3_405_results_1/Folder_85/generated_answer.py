def return_vowels(s):
    vowels = 'AEIOUaeiou'
    result = [char for i, char in enumerate(s[55:65]) if char in vowels and 'Z' < char <= 'w']
    return result