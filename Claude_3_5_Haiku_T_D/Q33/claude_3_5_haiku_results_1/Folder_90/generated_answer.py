def return_vowels(string):
    vowels = 'aeiouAEIOU'
    result = []
    for i in range(142, 145):
        if i < len(string):
            char = string[i]
            if char in vowels and char > '4' and (char <= 'o'):
                result.append(char)
    return result