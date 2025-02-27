def return_vowels(sentence):
    vowels = ['a', 'e', 'i', 'o', 'u']
    specified_range = sentence[604:949]
    result = [char for char in specified_range if char > 'n' and char <= 'u' and (char in vowels)]
    return result if result else []