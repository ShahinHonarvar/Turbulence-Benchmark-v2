def return_vowels(string):
    vowels = 'aeiouAEIOU'
    result = []
    for i in range(2, 7):
        if i < len(string) and string[i] in vowels and ('^' < string[i] <= 'd'):
            result.append(string[i])
    return result