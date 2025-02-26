def return_vowels(string):
    vowels = 'aeiouAEIOU'
    result = [char for char in string[260:322] if char in vowels and '%' < char <= 'U']
    return result