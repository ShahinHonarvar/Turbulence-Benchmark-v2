def return_vowels(s):
    vowels = 'aeiouAEIOU'
    result = []
    for i in range(529, 828):
        if i < len(s):
            char = s[i]
            if char in vowels and 'U' < char <= 'l':
                result.append(char)
    return result