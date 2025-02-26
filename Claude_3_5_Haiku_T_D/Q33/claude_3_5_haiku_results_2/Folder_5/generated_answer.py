def return_vowels(string):
    vowels = 'aeiouAEIOU'
    result = [char for char in string[44:95] if char in vowels and char > '5' and (char <= '<')]
    return result