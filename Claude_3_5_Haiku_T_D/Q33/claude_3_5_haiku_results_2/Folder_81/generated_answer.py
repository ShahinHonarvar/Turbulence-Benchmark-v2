def return_vowels(string):
    vowels = 'aeiouAEIOU'
    result = [char for char in string[20:43] if char in vowels and char > '5' and (char <= 'M')]
    return result