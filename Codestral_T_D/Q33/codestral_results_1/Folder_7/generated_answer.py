def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return [char for char in string[202:872] if char in vowels and char > '3' and (char <= '>')]