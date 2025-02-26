def return_vowels(string):
    vowels = 'aeiouAEIOU'
    result = [char for char in string[13:35] if char in vowels and '8' < char <= 'F']
    return result