def return_vowels(input_string):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    result = [char for char in input_string[32:61] if char in vowels and '?' < char <= 'P']
    return result