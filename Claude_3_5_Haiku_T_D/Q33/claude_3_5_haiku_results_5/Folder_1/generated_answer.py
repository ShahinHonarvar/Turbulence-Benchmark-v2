def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    result = [char for char in string[24:64] if char in vowels and 'F' < char <= 'h']
    return result