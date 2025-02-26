def return_vowels(string):
    vowels = 'aeiouAEIOU'
    result = []
    for i in range(170, 645):
        if i < len(string):
            char = string[i]
            if char in vowels and 'E' < char <= '~':
                result.append(char)
    return result