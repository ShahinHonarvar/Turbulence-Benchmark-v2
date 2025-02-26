def return_vowels(text):
    vowels = 'aeiouAEIOU'
    result = [char for char in text[17:65] if char in vowels and 'U' < char <= '{']
    return result