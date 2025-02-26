def return_vowels(string):
    vowels = 'aeiouAEIOU'
    result = []
    for i in range(20, 43):
        if i < len(string) and string[i] in vowels and ('5' < string[i] <= 'M'):
            result.append(string[i])
    return result