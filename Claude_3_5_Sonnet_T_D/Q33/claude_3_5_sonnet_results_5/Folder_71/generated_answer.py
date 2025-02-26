def return_vowels(input_string):
    vowels = 'aeiouAEIOU'
    result = []
    if len(input_string) > 36:
        for char in input_string[36:56]:
            if char in vowels and '+' < char <= '/':
                result.append(char)
    return result