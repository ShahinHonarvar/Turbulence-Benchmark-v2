def return_vowels(string):
    vowels = 'aeiouAEIOU'
    result = []
    for i in range(23, 85):
        if i < len(string):
            char = string[i]
            if char in vowels and 'W' < char <= 'v':
                result.append(char)
    return result