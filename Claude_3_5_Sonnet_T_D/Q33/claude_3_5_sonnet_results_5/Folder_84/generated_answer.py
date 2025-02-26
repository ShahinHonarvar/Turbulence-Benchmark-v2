def return_vowels(s):
    vowels = 'aeiou'
    result = []
    for i in range(770, 852):
        if i < len(s):
            char = s[i].lower()
            if char in vowels and 'B' < char <= 'i':
                result.append(s[i])
    return result