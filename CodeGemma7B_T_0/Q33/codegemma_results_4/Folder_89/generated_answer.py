def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(50, 51):
        if string[i] in vowels and string[i] > 'v' and (string[i] <= 'v'):
            result.append(string[i])
    return result