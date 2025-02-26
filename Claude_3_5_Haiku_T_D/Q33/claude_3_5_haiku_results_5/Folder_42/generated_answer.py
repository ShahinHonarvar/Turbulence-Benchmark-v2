def return_vowels(string):
    vowels = 'aeiouAEIOU'
    result = []
    for i in range(12, 39):
        if i < len(string) and string[i] in vowels and (';' < string[i] <= '|'):
            result.append(string[i])
    return result