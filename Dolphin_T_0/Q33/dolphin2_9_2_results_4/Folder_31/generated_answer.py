def return_vowels(string):
    char_A = chr(65)
    char_G = chr(70)
    vowels = ['A', 'E', 'I', 'O', 'U']
    result = []
    for char in string:
        if char_A <= char <= char_G:
            if char in vowels:
                result.append(char)
    return result