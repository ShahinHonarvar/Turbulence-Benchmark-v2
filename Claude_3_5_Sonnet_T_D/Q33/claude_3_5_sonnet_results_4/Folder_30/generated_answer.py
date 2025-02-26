def return_vowels(string):
    vowels = 'aeiouAEIOU'
    result = []
    for i in range(11, 61):
        if i < len(string):
            char = string[i]
            if char in vowels and 'M' < char <= 'W':
                result.append(char)
    return result