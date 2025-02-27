def return_vowels(string):
    vowels = ['A', 'E', 'I', 'O', 'U']
    return [char for char in string[32:61] if char > '?' and char <= 'P' and (char in vowels)]