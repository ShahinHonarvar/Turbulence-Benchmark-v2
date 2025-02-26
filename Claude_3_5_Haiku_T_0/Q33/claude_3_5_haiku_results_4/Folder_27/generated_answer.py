def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = [char for char in string[29:31] if char in vowels and 'a' < char <= 'f']
    return result