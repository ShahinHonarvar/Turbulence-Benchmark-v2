def return_vowels(input_string):
    vowels = 'aeiouAEIOU'
    result = []
    if len(input_string) > 5:
        char = input_string[5]
        if char in vowels and '3' < char <= '^':
            result.append(char)
    return result