def return_vowels(input_string):
    vowels = 'aeiouAEIOU'
    result = []
    for char in input_string[3:8]:
        if char in vowels and ';' < char <= 'D':
            result.append(char)
    return result