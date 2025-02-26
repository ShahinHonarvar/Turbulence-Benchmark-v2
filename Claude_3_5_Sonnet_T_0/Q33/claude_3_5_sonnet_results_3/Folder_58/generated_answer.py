def return_vowels(string):
    vowels = 'aeiouAEIOU'
    result = []
    for i in range(260, 322):
        if i < len(string):
            char = string[i]
            if char in vowels and '%' < char <= 'U':
                result.append(char)
    return result