def return_vowels(string):
    vowels = 'aeiouAEIOU'
    return [char for char in string[328:455] if char in vowels and '<' < char <= 'z']