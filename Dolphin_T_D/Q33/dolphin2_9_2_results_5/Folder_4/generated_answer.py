def return_vowels(string):
    vowels = ['A', 'E', 'I', 'O', 'U']
    result = []
    for char in string[40:91]:
        if char > 'A' and char <= 'x':
            if char in vowels:
                result.append(char)
    return result