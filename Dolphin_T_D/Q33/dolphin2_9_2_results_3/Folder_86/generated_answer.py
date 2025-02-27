def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for char in string[273:275]:
        if char > '+' and char <= 'o':
            if char in vowels:
                result.append(char)
    return result