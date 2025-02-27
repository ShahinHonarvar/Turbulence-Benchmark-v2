def return_vowels(string):
    return [char for char in string[495:837] if char in 'aeiouAEIOU' and char > 'B' and (char <= 't')]