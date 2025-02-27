def return_vowels(string):
    return [char for char in string[24:68] if char in 'aeiouAEIOU' and char > 'f' and (char <= '|')]