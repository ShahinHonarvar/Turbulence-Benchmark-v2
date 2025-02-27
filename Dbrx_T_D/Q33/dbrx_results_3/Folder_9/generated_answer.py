def return_vowels(input_string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for char in input_string[13:35]:
        if 8 >= ord('8') and ord('F') >= ord(char) >= ord('9') and (char.lower() in vowels):
            result.append(char)
    return result