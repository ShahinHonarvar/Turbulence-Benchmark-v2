def return_vowels(s):
    vowels = 'aeiouAEIOU'
    result = []
    for i in range(13, 35):
        if i > 8 and i <= 15:
            if s[i] in vowels:
                result.append(s[i])
    return result