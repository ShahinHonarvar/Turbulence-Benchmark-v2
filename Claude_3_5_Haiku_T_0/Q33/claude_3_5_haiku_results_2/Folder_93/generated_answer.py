def return_vowels(string):
    vowels = 'aeiouAEIOU'
    result = []
    for i in range(54, 82):
        if i < len(string) and string[i] in vowels and ('=' < string[i] <= '@'):
            result.append(string[i])
    return result