def return_vowels(string):
    return [char for char in string[69:82] if char in 'aeiouAEIOU' and char > '[' and (char <= '~')]