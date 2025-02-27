def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(len(string)):
        if 3 <= i < 8 and string[i] in vowels:
            if string[i] > ';' and string[i] <= 'D':
                result.append(string[i])
    return result