def return_vowels(string):
    vowels = ['A', 'E', 'I', 'O', 'U']
    result = []
    for char in string[1:4]:
        if char > 'C' and char <= 'I' and (char.upper() in vowels):
            result.append(char)
    return result