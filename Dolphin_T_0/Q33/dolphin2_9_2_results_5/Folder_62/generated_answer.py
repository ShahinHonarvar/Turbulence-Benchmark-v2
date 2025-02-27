def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for char in string[14:60]:
        if char > 'D' and char <= 'v':
            if char in vowels:
                result.append(char)
    return result