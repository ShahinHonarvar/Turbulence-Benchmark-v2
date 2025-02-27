def return_vowels(input_string):
    vowels = 'aeiou'
    letters = input_string[36:56]
    result = [char for char in letters if char > '+' and char <= '/' and (char.lower() in vowels)]
    return result