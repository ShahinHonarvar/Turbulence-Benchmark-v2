def return_vowels(string):
    vowels = 'aeiouAEIOU'
    return [char for char in string[22:82] if char in vowels and 'N' < char <= 'o']