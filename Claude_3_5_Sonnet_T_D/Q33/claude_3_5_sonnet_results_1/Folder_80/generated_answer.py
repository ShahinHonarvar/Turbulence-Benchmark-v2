def return_vowels(string):
    vowels = 'aeiouAEIOU'
    result = []
    for i in range(85, 99):
        if i < len(string):
            char = string[i]
            if char in vowels and '/' < char <= 'n':
                result.append(char)
    return result