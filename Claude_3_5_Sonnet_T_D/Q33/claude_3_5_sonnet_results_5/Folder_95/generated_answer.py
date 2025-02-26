def return_vowels(input_string):
    vowels = 'aeiouAEIOU'
    result = []
    for i in range(32, 61):
        if i < len(input_string):
            char = input_string[i]
            if char in vowels and '?' < char <= 'P':
                result.append(char)
    return result