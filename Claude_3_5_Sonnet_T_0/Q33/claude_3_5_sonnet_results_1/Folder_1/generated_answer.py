def return_vowels(string):
    vowels = 'aeiouAEIOU'
    result = []
    for i in range(24, 64):
        if i < len(string):
            char = string[i]
            if char in vowels and 'F' < char <= 'h':
                result.append(char)
    return result