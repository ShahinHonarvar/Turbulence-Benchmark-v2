def return_vowels(string):
    vowels = 'aeiou'
    result = []
    for i in range(50, 77):
        if i < len(string):
            char = string[i]
            if char.lower() in vowels and ord('#') < ord(char.lower()) <= ord('r'):
                result.append(char)
    return result