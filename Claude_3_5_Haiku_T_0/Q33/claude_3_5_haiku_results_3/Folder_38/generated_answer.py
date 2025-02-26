def return_vowels(string):
    vowels = 'aeiouAEIOU'
    result = [char for char in string[17:65] if char in vowels and 'U' < char <= '{']
    return result