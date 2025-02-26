def return_vowels(input_string):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    result = []
    for index in range(20, 34):
        if index < len(input_string):
            char = input_string[index]
            if char in vowels and 'U' < char <= 'i':
                result.append(char)
    return result