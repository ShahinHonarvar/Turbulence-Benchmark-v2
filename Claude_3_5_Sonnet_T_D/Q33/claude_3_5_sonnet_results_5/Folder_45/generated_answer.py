def return_vowels(input_string):
    vowels = 'aeiouAEIOU'
    result = []
    for i in range(43, 70):
        if i < len(input_string):
            char = input_string[i]
            if char in vowels and '*' < char <= 'b':
                result.append(char)
    return result