def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    filtered = [char for char in string[12:39] if char in vowels and char > ';' and (char <= '|')]
    return filtered