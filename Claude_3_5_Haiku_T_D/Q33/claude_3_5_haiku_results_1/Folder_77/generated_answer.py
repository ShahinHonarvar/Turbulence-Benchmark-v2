def return_vowels(string):
    vowels = 'aeiouAEIOU'
    result = [char for char in string[837:975] if char in vowels and 'N' < char <= 'W']
    return result