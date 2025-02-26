def return_vowels(string):
    vowels = 'aeiouAEIOU'
    result = [char for char in string[20:41] if char in vowels and 'K' < char <= 'Z']
    return result