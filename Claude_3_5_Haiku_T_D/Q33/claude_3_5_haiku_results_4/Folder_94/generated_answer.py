def return_vowels(string):
    vowels = 'aeiouAEIOU'
    result = [char for char in string[40:94] if char in vowels and '4' < char <= 'H']
    return result