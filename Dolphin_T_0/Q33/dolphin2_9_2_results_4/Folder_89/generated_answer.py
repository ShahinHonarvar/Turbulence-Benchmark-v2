def return_vowels(input_string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for char in input_string[50:51]:
        if char in vowels and char >= 'a' and (char <= 'v'):
            result.append(char)
    return result