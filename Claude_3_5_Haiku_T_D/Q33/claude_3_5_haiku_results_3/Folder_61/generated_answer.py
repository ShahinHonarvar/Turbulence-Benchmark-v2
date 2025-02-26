def return_vowels(string):
    vowels = 'aeiouAEIOU'
    result = []
    for i in range(1, 4):
        if i < len(string) and string[i] in vowels and ('C' < string[i] <= 'I'):
            result.append(string[i])
    return result