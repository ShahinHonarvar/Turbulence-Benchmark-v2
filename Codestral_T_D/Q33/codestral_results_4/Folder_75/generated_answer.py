def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return [char for char in string[20:41] if char > 'k' and char <= 'z' and (char in vowels)]