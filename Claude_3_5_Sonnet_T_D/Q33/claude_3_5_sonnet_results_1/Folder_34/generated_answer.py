def return_vowels(input_string):
    vowels = 'aeiouAEIOU'
    result = []
    for char in input_string[19:32]:
        if char in vowels and '0' < char <= '7':
            result.append(char)
    return result