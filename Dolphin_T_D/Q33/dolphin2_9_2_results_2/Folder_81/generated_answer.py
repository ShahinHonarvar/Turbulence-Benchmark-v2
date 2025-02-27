def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(20, 43):
        if 'J' < string[i] <= 'M' and string[i] in vowels:
            result.append(string[i])
    return result