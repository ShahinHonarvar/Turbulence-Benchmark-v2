def return_vowels(input_string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for char in input_string[71:88]:
        if 'a' <= char <= 'p' and char in vowels:
            result.append(char)
    return result