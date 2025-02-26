def return_vowels(string):
    vowels = 'aeiouAEIOU'
    result = []
    for i in range(74, 96):
        if i < len(string):
            char = string[i]
            if char in vowels and 'I' < char <= 'X':
                result.append(char)
    return result