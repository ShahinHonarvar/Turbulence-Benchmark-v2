def return_vowels(input_string):
    vowels = 'aeiouAEIOU'
    result = []
    for i in range(63, 79):
        if i < len(input_string):
            char = input_string[i]
            if char in vowels and 'D' < char <= 'y':
                result.append(char)
    return result