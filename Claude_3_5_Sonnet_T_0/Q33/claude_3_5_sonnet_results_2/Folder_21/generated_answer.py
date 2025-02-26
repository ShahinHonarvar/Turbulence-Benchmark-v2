def return_vowels(string):
    vowels = 'aeiou'
    result = []
    for i in range(464, 574):
        if i < len(string):
            char = string[i].lower()
            if char in vowels and 'a' < char <= 'g':
                result.append(string[i])
    return result