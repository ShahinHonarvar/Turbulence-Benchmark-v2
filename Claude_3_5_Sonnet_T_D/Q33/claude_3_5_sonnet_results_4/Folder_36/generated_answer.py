def return_vowels(input_string):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    result = []
    for i in range(604, 949):
        if i < len(input_string):
            char = input_string[i]
            if char in vowels and 'N' < char <= 'U':
                result.append(char)
    return result