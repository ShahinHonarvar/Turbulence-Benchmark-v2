def return_vowels(string):
    vowels = 'aeiou'
    result = [string[i] for i in range(4, 8) if vowels.contains(string[i]) and string[i] > 'P' and (string[i] <= 'r')]
    return result