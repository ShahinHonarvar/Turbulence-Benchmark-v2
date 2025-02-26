def return_vowels(string):
    vowels = 'aeiou'
    result = []
    for i in range(483, 664):
        if i < len(string):
            char = string[i].lower()
            if char in vowels and '&' < char <= 'h':
                result.append(string[i])
    return result