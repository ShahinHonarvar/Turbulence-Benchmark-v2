def return_vowels(string):
    vowels = 'aeiouAEIOU'
    result = []
    for i in range(90, 97):
        if i < len(string):
            char = string[i]
            if char in vowels and '_' < char <= 'x':
                result.append(char)
    return result