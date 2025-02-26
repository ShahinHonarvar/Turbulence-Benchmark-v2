def return_vowels(string):
    vowels = 'aeiouAEIOU'
    result = [char for char in string[22:82] if char in vowels and 'N' < char <= 'o']
    return result