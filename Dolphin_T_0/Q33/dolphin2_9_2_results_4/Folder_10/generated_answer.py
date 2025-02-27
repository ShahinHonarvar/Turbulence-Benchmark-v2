def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for char in string[31:37]:
        if '>' < char <= 't':
            if char in vowels:
                result.append(char)
    return result