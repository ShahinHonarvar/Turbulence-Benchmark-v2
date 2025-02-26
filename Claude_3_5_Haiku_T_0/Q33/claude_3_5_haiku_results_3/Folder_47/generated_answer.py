def return_vowels(string):
    vowels = 'aeiouAEIOU'
    result = [char for char in string[23:38] if char in vowels and char > 'N' and (char <= 'k')]
    return result