def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return [char for char in string[142:145] if char in vowels and char > '4' and (char <= 'o')]