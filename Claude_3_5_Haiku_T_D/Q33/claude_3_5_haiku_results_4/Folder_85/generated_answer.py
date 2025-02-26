def return_vowels(text):
    vowels = 'aeiou'
    result = [char for char in text[55:65] if char in vowels and 'Z' < char <= 'w']
    return result