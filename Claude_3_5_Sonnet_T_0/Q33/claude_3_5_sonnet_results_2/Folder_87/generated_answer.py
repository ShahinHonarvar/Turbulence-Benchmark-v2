def return_vowels(string):
    vowels = 'aeiou'
    result = []
    for i in range(34, 58):
        if i < len(string):
            char = string[i].lower()
            if char in vowels and 'b' < char <= 'o':
                result.append(string[i])
    return result