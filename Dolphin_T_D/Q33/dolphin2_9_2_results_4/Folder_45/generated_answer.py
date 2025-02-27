def return_vowels(input_string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for char in input_string[43:70]:
        if char > '*' and char <= 'b' and (char in vowels):
            result.append(char)
    return result