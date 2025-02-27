def return_vowels(string):
    return [char for char in string[770:852] if char in 'aeiouAEIOU' and char > 'B' and (char <= 'i')]