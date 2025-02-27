def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(14, 60):
        if string[i] in vowels and string[i] > 'D' and (string[i] <= 'v'):
            result.append(string[i])
    return result