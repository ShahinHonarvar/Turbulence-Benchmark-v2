def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for char in string[74:96]:
        if char > 'I' and char <= 'X':
            if char in vowels:
                result.append(char)
    return result