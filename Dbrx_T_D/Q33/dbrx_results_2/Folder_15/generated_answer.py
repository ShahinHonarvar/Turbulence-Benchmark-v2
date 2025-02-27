def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = [char for char in string[5:6] if char > '3' and char <= '^' and (char in vowels)]
    return result