def return_vowels(input_string):
    vowels = 'aeiouAEIOU'
    result = []
    for i in range(90, 97):
        if i < len(input_string):
            char = input_string[i]
            if char in vowels and '_' < char <= 'x':
                result.append(char)
    return result