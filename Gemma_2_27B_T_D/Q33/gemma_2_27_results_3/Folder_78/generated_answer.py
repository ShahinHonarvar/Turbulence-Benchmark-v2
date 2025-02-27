def return_vowels(string):
    return [char for char in string[46:90] if char in 'aeiouAEIOU' and char > '@' and (char <= '[')]