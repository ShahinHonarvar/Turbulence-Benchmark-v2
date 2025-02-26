def return_vowels(string):
    vowels = 'aeiou'
    result = []
    for i in range(770, 852):
        if i < len(string):
            char = string[i]
            if char.lower() in vowels and 'B' < char <= 'i':
                result.append(char)
    return result