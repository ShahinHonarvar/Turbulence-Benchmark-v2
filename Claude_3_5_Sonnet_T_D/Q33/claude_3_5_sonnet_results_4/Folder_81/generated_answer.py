def return_vowels(input_string):
    vowels = 'aeiouAEIOU'
    result = []
    for char in input_string[20:43]:
        if char in vowels and '5' < char <= 'M':
            result.append(char)
    return result