def return_vowels(string):
    return [char for char in string[19:20] if char in 'aeiouAEIOU' and char > '<' and (char <= 'p')]