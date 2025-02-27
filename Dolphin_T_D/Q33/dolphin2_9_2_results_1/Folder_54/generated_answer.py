def return_vowels(string):
    vowels = 'aeiou'
    result = [string[i] for i in range(23, 85) if string[i] > 'W' and string[i] <= 'v' and (string[i] in vowels)]
    return result