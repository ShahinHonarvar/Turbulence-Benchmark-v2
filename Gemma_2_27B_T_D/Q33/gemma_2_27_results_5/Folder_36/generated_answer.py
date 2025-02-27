def return_vowels(text):
    vowels = 'AEIOU'
    return [char for char in text[604:949] if char in vowels and char > 'N' and (char <= 'U')]