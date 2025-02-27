def return_vowels(input_str):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for char in input_str:
        if char >= 'Q' and char <= ']':
            if char in vowels:
                result.append(char)
    return result