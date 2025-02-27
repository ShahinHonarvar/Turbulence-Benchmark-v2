def return_vowels(input_string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for character in input_string[77:84]:
        if '(' < character <= 'G' and character in vowels:
            result.append(character)
    return result