def return_vowels(input_string):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    result = [char for char in input_string[23:38] if char in vowels and 'N' < char <= 'k']
    return result