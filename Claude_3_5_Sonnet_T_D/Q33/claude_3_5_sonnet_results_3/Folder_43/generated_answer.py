def return_vowels(input_string):
    vowels = 'aeiouAEIOU'
    result = []
    for char in input_string[22:82]:
        if char in vowels and 'N' < char <= 'o':
            result.append(char)
    return result