def return_vowels(input_string):
    vowels = 'aeiouAEIOU'
    result = []
    for i in range(495, 837):
        if i < len(input_string):
            char = input_string[i]
            if char in vowels and 'B' < char <= 't':
                result.append(char)
    return result