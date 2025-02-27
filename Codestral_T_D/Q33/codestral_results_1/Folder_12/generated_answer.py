def return_vowels(input_string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for char in input_string[13:37]:
        if 'Z' < char < '}':
            if char in vowels:
                result.append(char)
    return result