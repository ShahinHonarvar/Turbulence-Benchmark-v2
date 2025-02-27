def return_vowels(input_string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for char in input_string[11:53]:
        if char > '+' and char <= 'W':
            if char.lower() in vowels:
                result.append(char)
    return result