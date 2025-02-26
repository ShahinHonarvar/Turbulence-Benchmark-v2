def return_vowels(s):
    vowels = 'aeiou'
    result = []
    for i in range(24, 64):
        if i < len(s):
            if s[i].lower() in vowels and 'F' < s[i] <= 'h':
                result.append(s[i])
    return result