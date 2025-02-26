def return_vowels(string):
    vowels = 'aeiouAEIOU'
    result = []
    for i in range(3, 8):
        if i < len(string) and string[i] in vowels and (';' < string[i] <= 'D'):
            result.append(string[i])
    return result