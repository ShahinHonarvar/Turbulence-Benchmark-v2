def return_vowels(input_string):
    """Function 'return_vowels' that takes one argument, a string"""
    input_string = input_string[8:9]
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = [x for x in input_string if x in vowels and x > 'Y' and (x <= 's')]
    return result