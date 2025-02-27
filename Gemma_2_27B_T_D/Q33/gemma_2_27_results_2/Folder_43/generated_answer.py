def return_vowels(string):
    return [char for char in string[22:82] if char in 'aeiouAEIOU' and char > 'N' and (char <= 'o')]