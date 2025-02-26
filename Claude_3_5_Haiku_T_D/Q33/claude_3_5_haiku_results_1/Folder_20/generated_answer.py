def return_vowels(input_string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for index in range(59, 61):
        if index < len(input_string):
            char = input_string[index].lower()
            if char in vowels and '+' < char <= 'h':
                result.append(char)
    return result