def return_vowels(s):
    vowels = 'aeiouAEIOU'
    result = []
    for i in range(529, 828):
        if i < len(s) and s[i] in vowels and ('U' < s[i] <= 'l'):
            result.append(s[i])
    return result