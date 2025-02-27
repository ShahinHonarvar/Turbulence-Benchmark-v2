def return_vowels(string):
    vowels = 'AEIOUaeiou'
    result = []
    for i in range(65, 70):
        if string[i] in vowels and string[i] not in ['%', 'G', 'g']:
            result.append(string[i])
    return result