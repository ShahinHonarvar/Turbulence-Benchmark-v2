def return_vowels(string):
    vowels = 'aeiouAEIOU'
    result = []
    for i in range(43, 70):
        if i < len(string):
            char = string[i]
            if char in vowels and '*' < char <= 'b':
                result.append(char)
    return result