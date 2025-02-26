def return_vowels(input_string):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    result = [char for char in input_string[13:37] if char in vowels and ord('Z') < ord(char) <= ord('}')]
    return result