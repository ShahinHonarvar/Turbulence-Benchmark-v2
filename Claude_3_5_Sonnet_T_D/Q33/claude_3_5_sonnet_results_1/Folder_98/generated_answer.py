def return_vowels(input_string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for char in input_string[3:9]:
        if char.lower() in vowels and 'S' < char <= 'U':
            result.append(char)
    return result