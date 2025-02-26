def return_vowels(input_string):
    vowels = 'aeiouAEIOU'
    result = []
    for index in range(13, 35):
        if index < len(input_string):
            char = input_string[index]
            if char in vowels and char > '8' and (char <= 'F'):
                result.append(char)
    return result