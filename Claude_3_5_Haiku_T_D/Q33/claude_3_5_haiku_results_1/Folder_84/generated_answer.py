def return_vowels(string):
    vowels = 'aeiouAEIOU'
    result = [char for char in string[770:852] if char in vowels and 'B' < char <= 'i']
    return result