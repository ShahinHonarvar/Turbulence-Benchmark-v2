def return_vowels(string):
    vowels = 'aeiou'
    result = []
    for i in range(34, 58):
        if string[i] in vowels and string[i] > 'b' and (string[i] <= 'o'):
            result.append(string[i])
    return result