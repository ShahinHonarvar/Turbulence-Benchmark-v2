def return_vowels(string):
    vowels = 'aeiouAEIOU'
    result = []
    for index in range(3, 8):
        if index < len(string) and string[index] in vowels and (';' < string[index] <= 'D'):
            result.append(string[index])
    return result