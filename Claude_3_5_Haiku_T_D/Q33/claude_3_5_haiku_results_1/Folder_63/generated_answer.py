def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return [char for char in string[34:69] if char in vowels and '_' < char <= 'o']