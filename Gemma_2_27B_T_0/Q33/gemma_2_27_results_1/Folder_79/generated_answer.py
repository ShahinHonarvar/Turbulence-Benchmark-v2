def return_vowels(string):
    return [char for char in string[74:96] if char in 'aeiouAEIOU' and char > 'I' and (char <= 'X')]