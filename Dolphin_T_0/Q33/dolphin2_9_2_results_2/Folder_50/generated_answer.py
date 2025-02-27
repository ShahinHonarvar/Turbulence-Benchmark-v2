def return_vowels(string):
    vowels = 'aeiou'
    return [string[i] for i in range(11, 53) if string[i] in vowels and string[i] > '+' and (string[i] <= 'W')]