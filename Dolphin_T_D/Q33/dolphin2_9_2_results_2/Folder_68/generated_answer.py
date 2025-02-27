def return_vowels(string):
    vowels = 'aeiou'
    return [string[i] for i in range(1, 9) if string[i] in vowels and string[i] > '?' and (string[i] <= 'k')]