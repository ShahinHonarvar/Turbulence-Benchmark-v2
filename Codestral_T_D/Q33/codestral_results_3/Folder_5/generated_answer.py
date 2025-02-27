def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = [char for char in string[44:95] if char > '5' and char <= '<' and (char in vowels)]
    return result