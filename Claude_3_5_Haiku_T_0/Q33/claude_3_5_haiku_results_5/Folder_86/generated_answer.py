def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(273, 275):
        if i < len(string):
            char = string[i]
            if char in vowels and '+' < char <= 'o':
                result.append(char)
    return result