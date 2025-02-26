def return_vowels(string):
    vowels = 'aeiouAEIOU'
    result = []
    for i in range(23, 57):
        if i < len(string):
            char = string[i]
            if char in vowels and '0' < char <= 'd':
                result.append(char)
    return result