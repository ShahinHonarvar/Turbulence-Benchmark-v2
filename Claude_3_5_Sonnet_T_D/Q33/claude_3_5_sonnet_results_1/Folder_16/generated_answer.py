def return_vowels(string):
    vowels = 'aeiou'
    result = []
    for i in range(133, 306):
        if i < len(string):
            char = string[i].lower()
            if char in vowels and 'c' < char <= 'd':
                result.append(string[i])
    return result