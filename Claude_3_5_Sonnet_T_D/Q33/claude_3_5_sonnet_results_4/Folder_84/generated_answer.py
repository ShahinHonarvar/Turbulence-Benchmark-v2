def return_vowels(s):
    vowels = 'aeiou'
    result = []
    for i in range(770, 852):
        if i < len(s):
            if s[i].lower() in vowels and 'B' < s[i] <= 'i':
                result.append(s[i])
    return result