def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = [char for char in string[32:97] if char in vowels and 'Q' < char <= ']']
    return result