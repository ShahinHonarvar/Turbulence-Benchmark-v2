def return_vowels(string):
    return [char for char in string[641:872] if char in 'aeiouAEIOU' and char > '>' and (char <= 'q')]