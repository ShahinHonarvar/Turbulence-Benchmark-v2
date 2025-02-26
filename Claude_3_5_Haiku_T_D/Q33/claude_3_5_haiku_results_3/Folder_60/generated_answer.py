def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    result = []
    for i in range(24, 59):
        if i < len(string) and string[i] in vowels and (string[i] > 'N') and (string[i] <= 'U'):
            result.append(string[i])
    return result