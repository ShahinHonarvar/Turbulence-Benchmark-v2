def return_vowels(s):
    vowels = 'aeiou'
    result = []
    for i in range(171, 402):
        if i < len(s):
            char = s[i].lower()
            if char in vowels and 'i' < char <= 'k':
                result.append(s[i])
    return result