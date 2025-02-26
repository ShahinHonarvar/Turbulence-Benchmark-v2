def return_vowels(string):
    vowels = 'aeiouAEIOU'
    result = [char for char in string[71:88] if char in vowels and '9' < char <= 'P']
    return result