def return_vowels(text):
    vowels = 'aeiouAEIOU'
    result = [char for char in text[86:99] if char in vowels and 'E' < char <= 'r']
    return result