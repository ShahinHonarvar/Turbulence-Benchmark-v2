def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for char in string[44:95]:
        if char > '5' and char <= '<':
            if char in vowels:
                result.append(char)
    return result