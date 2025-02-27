def return_vowels(string):
    vowels = 'aeiouAEIOU'
    result = [char for char in string[46:90] if char in vowels and '@' < char <= '[']
    return result