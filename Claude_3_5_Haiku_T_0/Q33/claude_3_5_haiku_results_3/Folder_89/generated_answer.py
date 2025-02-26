def return_vowels(string):
    vowels = 'aeiouAEIOU'
    result = [char for char in string[50:51] if char in vowels and ',' < char <= 'v']
    return result