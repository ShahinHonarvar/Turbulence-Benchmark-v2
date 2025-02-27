def return_vowels(s):
    vowels = ['A', 'E', 'I', 'O', 'U']
    specified_range = s[41:50]
    result = [char for char in specified_range if char > 'W' and char <= '[']
    return [char for char in result if char in vowels]