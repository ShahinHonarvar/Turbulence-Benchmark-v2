def return_vowels(string):
    vowels = 'aeiouAEIOU'
    result = [char for char in string[24:68] if char in vowels and 'f' < char <= '|']
    return result