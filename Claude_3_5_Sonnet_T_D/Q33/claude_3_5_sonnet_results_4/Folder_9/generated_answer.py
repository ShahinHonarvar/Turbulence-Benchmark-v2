def return_vowels(string):
    vowels = 'aeiouAEIOU'
    result = []
    for i in range(13, 35):
        if i < len(string):
            char = string[i]
            if char in vowels and '8' < char <= 'F':
                result.append(char)
    return result