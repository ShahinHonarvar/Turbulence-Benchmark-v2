def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = [char for char in string[19:20] if char in vowels and '<' < char <= 'p']
    return result