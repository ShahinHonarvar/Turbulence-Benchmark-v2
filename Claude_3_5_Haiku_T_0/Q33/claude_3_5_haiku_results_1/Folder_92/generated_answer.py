def return_vowels(string):
    vowels = 'aeiouAEIOU'
    result = [char for char in string[3:8] if char in vowels and ';' < char <= 'D']
    return result