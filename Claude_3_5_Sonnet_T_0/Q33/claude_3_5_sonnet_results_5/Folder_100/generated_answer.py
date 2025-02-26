def return_vowels(string):
    vowels = 'aeiouAEIOU'
    result = []
    for i in range(23, 75):
        if i < len(string):
            char = string[i]
            if char in vowels and 'L' < char <= 'd':
                result.append(char)
    return result