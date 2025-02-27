def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(11, 53):
        if string[i] in vowels:
            if 'a' <= string[i] <= 'z':
                result.append(string[i])
    return result