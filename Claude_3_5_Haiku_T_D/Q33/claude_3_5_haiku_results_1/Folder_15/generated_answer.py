def return_vowels(input_string):
    vowels = 'aeiouAEIOU'
    result = []
    for i in range(5, 6):
        if i < len(input_string):
            char = input_string[i]
            if char in vowels and '3' < char <= '^':
                result.append(char)
    return result