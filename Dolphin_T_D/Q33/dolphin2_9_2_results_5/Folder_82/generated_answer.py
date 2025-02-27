def return_vowels(string):
    vowels = ['A', 'E', 'I', 'O', 'U']
    result = []
    for char in string[86:99]:
        if 'E' < char <= 'r' and char.upper() in vowels:
            result.append(char)
    return result