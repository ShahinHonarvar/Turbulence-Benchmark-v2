def return_vowels(string):
    vowels = 'aeiou'
    result = []
    for i in range(529, 828):
        if i < len(string):
            char = string[i].lower()
            if char in vowels and 'u' < char <= 'l':
                result.append(string[i])
    return result