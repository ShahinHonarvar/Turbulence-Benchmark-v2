def return_vowels(input_string):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    result = [char for char in input_string[82:90] if char in vowels and ord(char) > ord('T') and (ord(char) <= ord('b'))]
    return result