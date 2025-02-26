def return_vowels(string):
    result = []
    for i in range(273, 275):
        if i < len(string):
            char = string[i]
            if char > '+' and char <= 'o' and (char in 'aeiouAEIOU'):
                result.append(char)
    return result