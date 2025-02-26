def return_vowels(string):
    vowels = 'aeiouAEIOU'
    result = []
    for i in range(71, 88):
        if i < len(string) and string[i] in vowels and ('9' < string[i] <= 'P'):
            result.append(string[i])
    return result