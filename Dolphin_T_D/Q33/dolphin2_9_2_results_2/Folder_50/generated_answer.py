def return_vowels(string):
    vowels = 'AEIOU'
    output = []
    for i in range(11, 53):
        if string[i] in vowels and string[i] > '+' and (string[i] <= 'W'):
            output.append(string[i])
    return output