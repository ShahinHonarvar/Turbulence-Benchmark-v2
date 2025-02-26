def return_vowels(string):
    vowels = 'aeiou'
    result = []
    for i in range(770, 852):
        if i < len(string):
            char = string[i].lower()
            if char in vowels and 'B' < char <= 'i':
                result.append(string[i])
    return result