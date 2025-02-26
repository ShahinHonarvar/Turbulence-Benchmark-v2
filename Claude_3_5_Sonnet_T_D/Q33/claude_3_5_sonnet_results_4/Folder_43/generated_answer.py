def return_vowels(input_string):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    result = []
    for char in input_string[22:82]:
        if char in vowels and 'N' < char <= 'o':
            result.append(char)
    return result