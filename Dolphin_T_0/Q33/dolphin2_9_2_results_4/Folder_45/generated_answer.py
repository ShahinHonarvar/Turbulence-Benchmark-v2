def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = [char for char in string[43:70] if char > '*' and char <= 'b' and (char in vowels)]
    return result