def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(46, 49):
        if i < len(string) and string[i] > '[' and (string[i] <= 'p') and (string[i] in vowels):
            result.append(string[i])
    return result