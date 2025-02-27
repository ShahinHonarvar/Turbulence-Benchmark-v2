def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for char in string[71:81]:
        if '>' < char <= 'U':
            if char in vowels:
                result.append(char)
    return result