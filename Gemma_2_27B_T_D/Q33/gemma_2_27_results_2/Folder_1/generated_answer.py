def return_vowels(string):
    return [char for char in string[24:64] if char in 'aeiouAEIOU' and char > 'F' and (char <= 'h')]