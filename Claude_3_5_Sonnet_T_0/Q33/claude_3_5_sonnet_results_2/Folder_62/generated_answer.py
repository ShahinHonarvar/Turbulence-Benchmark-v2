def return_vowels(string):
    vowels = 'aeiouAEIOU'
    result = []
    for i in range(14, 60):
        if i < len(string):
            char = string[i]
            if char in vowels and 'D' < char <= 'v':
                result.append(char)
    return result