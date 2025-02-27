def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(43, 70):
        if string[i] in vowels and string[i] > '*' and (string[i] <= 'b'):
            result.append(string[i])
    return result