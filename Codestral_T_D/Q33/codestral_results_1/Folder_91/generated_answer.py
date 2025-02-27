def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(4, 8):
        if i < len(string) and string[i] in vowels and (string[i] > 'P') and (string[i] <= 'r'):
            result.append(string[i])
    return result