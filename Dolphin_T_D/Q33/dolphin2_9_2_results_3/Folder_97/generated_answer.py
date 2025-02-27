def return_vowels(string):
    vowels = 'aeiou'
    result = []
    for i in range(328, 455):
        if string[i] > '<' and string[i] <= 'z' and (string[i] in vowels):
            result.append(string[i])
    return result