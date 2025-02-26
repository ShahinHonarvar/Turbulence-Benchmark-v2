def return_vowels(input_string):
    vowels = 'aeiouAEIOU'
    result = []
    for i in range(56, 90):
        if i < len(input_string):
            char = input_string[i]
            if char in vowels and 'K' < char <= 'z':
                result.append(char)
    return result