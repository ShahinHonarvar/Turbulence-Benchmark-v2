def return_vowels(string):
    return [char for char in string[32:61] if char in 'aeiouAEIOU' and '?' < char <= 'P']