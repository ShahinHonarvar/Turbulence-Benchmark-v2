def return_vowels(text):
    vowels = 'aeiou'
    return [char for char in text[50:77] if char in vowels and 'n' < char <= 'r']