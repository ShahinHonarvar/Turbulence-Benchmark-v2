def return_vowels(string):
    vowels = ['A', 'E', 'I', 'O', 'U']
    result = []
    for char in string[604:949]:
        if 'N' < char <= 'U' and char.upper() in vowels:
            result.append(char)
    return result