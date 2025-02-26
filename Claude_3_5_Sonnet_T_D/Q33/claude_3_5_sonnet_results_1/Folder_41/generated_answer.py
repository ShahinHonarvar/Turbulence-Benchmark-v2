def return_vowels(string):
    vowels = 'aeiouAEIOU'
    result = []
    for i in range(71, 81):
        if i < len(string):
            char = string[i]
            if char in vowels and '>' < char <= 'U':
                result.append(char)
    return result