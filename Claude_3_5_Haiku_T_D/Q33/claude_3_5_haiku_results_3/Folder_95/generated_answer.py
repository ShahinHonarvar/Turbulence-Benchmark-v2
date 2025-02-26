def return_vowels(string):
    vowels = 'aeiouAEIOU'
    return [char for char in string[32:61] if char in vowels and '?' < char <= 'P']