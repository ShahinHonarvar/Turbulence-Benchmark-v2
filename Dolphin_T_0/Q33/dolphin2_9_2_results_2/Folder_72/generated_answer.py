def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for char in string[37:57]:
        if char > '*' and char <= 'P':
            if char in vowels:
                result.append(char)
    return result