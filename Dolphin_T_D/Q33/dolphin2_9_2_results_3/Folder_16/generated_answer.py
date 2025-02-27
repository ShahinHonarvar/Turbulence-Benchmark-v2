def return_vowels(string, c, d):
    vowels = ['a', 'e', 'i', 'o', 'u']
    specified_range = string[133:306]
    result = [char for char in specified_range if c < char <= d and char in vowels]
    return result