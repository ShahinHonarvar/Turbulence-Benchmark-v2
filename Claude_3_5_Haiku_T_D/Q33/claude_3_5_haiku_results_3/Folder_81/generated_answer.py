def return_vowels(text):
    vowels = 'aeiouAEIOU'
    result = [char for char in text[20:43] if char in vowels and '5' < char <= 'M']
    return result