def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for char in string[19:20]:
        if '<' < char <= 'p':
            if char in vowels:
                result.append(char)
    return result