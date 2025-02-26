def return_vowels(string):
    vowels = 'aeiouAEIOU'
    result = []
    for i in range(24, 59):
        if i < len(string):
            char = string[i]
            if char in vowels and 'N' < char <= 'U':
                result.append(char)
    return result