def return_vowels(string):
    vowels = 'aeiouAEIOU'
    result = []
    for i in range(59, 61):
        if i < len(string) and string[i] in vowels and ('+' < string[i] <= 'h'):
            result.append(string[i])
    return result