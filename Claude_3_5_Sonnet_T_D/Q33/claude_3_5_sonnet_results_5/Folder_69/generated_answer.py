def return_vowels(input_string):
    vowels = 'aeiouAEIOU'
    result = []
    for i in range(641, 872):
        if i < len(input_string):
            char = input_string[i]
            if char in vowels and '>' < char <= 'q':
                result.append(char)
    return result