def return_vowels(string):
    vowels = 'aeiouAEIOU'
    return [char for char in string[260:322] if char in vowels and '%' < char <= 'U']