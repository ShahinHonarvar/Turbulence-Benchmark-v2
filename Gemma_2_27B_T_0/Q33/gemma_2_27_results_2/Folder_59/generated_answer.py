def return_vowels(string):
    return [char for char in string[8:9] if char in 'aeiouAEIOU' and char > 'Y' and (char <= 's')]