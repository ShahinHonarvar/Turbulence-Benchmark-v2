def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return [char for char in string[56:90] if char > 'K' and char <= 'z' and (char in vowels)]