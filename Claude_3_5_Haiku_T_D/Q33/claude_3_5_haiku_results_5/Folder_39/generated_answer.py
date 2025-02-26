def return_vowels(string):
    vowels = 'aeiouAEIOU'
    result = [char for char in string[32:97] if char in vowels and 'Q' < char <= ']']
    return result