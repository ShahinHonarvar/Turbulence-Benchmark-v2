def return_vowels(string):
    vowels = 'aeiouAEIOU'
    result = []
    for i in range(28, 76):
        if i < len(string):
            char = string[i]
            if char in vowels and '+' < char <= 'z':
                result.append(char)
    return result