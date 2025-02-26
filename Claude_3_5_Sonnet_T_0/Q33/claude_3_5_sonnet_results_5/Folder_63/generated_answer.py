def return_vowels(string):
    vowels = 'aeiou'
    result = []
    for i in range(34, 69):
        if i < len(string):
            char = string[i].lower()
            if char in vowels and '_' < char <= 'o':
                result.append(char)
    return result