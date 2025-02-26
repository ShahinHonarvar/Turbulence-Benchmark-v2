def return_vowels(input_string):
    vowels = 'aeiouAEIOU'
    result = []
    for i in range(24, 68):
        if i < len(input_string):
            char = input_string[i]
            if char in vowels and 'f' < char <= '|':
                result.append(char)
    return result