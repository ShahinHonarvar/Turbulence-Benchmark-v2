def return_vowels(string):
    vowels = 'aeiouAEIOU'
    result = []
    for i in range(149, 313):
        if i < len(string):
            char = string[i]
            if char in vowels and 'M' < char <= 'j':
                result.append(char)
    return result