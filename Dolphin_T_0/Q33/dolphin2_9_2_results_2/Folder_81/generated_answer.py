def return_vowels(string):
    vowels = ['A', 'E', 'I', 'O', 'U']
    specified_range = string[20:43]
    result = [char for char in specified_range if 5 < ord(char) < ord('M') and char.upper() in vowels]
    return result if result else []