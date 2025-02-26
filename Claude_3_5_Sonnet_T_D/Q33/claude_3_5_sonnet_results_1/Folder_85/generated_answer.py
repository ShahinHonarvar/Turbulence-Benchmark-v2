def return_vowels(input_string):
    vowels = 'aeiouAEIOU'
    result = []
    for i in range(55, 65):
        if i < len(input_string):
            char = input_string[i]
            if char in vowels and 'Z' < char <= 'w':
                result.append(char)
    return result