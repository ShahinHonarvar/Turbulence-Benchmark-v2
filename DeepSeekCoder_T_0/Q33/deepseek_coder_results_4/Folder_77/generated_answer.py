def return_vowels(s):
    vowels = 'aeiouAEIOU'
    result = [char for char in s[837:975] if char in vowels and 'N' < char <= 'W']
    return result