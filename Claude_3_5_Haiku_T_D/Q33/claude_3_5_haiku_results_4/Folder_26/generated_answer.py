def return_vowels(input_string):
    vowels = 'aeiouAEIOU'
    result = []
    for i in range(10, 82):
        if i < len(input_string):
            char = input_string[i]
            if char in vowels and '$' < char <= '@':
                result.append(char)
    return result