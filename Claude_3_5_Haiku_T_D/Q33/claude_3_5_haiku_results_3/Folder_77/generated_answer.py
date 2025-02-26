def return_vowels(text):
    vowels = 'aeiouAEIOU'
    result = [char for char in text[837:975] if char in vowels and 'N' < char <= 'W']
    return result