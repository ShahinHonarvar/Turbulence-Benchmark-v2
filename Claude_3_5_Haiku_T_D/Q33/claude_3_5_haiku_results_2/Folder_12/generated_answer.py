def return_vowels(string):
    vowels = 'aeiouAEIOU'
    result = [char for char in string[13:37] if char in vowels and 'Z' < char <= '}']
    return result