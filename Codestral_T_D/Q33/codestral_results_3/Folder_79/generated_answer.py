def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    filtered_vowels = [char for char in string[74:96] if char in vowels and char > 'I' and (char <= 'X')]
    return filtered_vowels