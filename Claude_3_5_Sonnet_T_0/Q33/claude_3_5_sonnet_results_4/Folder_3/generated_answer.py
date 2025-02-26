def return_vowels(string):
    vowels = 'aeiouAEIOU'
    result = []
    for i in range(50, 77):
        if i < len(string):
            char = string[i]
            if char in vowels and '#' < char <= 'r':
                result.append(char)
    return result