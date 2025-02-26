def return_vowels(string):
    vowels = 'aeiouAEIOU'
    result = [char for char in string[40:94] if char in vowels and char > '4' and (char <= 'H')]
    return result