def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = [char for char in string[24:64] if char.lower() in vowels and 'f' < char.lower() <= 'h']
    return result