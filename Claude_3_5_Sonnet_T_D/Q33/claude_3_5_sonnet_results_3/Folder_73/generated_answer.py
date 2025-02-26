def return_vowels(input_string):
    vowels = 'aeiouAEIOU'
    result = []
    for i in range(47, 89):
        if i < len(input_string):
            char = input_string[i]
            if char in vowels and '@' < char <= 'n':
                result.append(char)
    return result