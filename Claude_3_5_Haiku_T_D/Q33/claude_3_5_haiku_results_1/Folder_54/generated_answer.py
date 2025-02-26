def return_vowels(text):
    vowels = 'aeiouAEIOU'
    result = [char for char in text[23:85] if char in vowels and 'W' < char <= 'v']
    return result