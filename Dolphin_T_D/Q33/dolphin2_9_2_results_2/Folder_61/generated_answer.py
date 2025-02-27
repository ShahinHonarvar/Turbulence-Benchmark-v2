def return_vowels(string):
    vowels = 'aeiou'
    sub_string = string[1:4]
    result = [char for char in sub_string if char.lower() in vowels and char > 'c' and (char <= 'i')]
    return result