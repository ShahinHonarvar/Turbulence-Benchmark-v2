def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    target_chars = [character for character in string[149:313] if 'M' < character <= 'j']
    result = [character for character in target_chars if character in vowels]
    return result