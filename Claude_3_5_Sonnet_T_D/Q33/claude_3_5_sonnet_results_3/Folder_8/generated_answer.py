def return_vowels(string):
    vowels = 'aeiouAEIOU'
    result = []
    for i in range(64, 82):
        if i < len(string):
            char = string[i]
            if char in vowels and 'P' < char <= 'z':
                result.append(char)
    return result