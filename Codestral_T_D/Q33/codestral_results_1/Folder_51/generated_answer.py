def return_vowels(string):
    vowels = ['A', 'E', 'I', 'O', 'U']
    result = []
    for char in string[56:68]:
        if char in vowels and char > 'M' and (char <= 'X'):
            result.append(char)
    return result