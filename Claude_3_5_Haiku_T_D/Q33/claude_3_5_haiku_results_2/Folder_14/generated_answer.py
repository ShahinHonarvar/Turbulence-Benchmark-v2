def return_vowels(string):
    vowels = 'aeiouAEIOU'
    result = [char for char in string[47:61] if char in vowels and '9' < char <= 'O']
    return result