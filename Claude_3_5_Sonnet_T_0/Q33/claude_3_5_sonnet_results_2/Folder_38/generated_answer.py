def return_vowels(string):
    vowels = 'aeiouAEIOU'
    result = []
    for i in range(17, 65):
        if i < len(string):
            char = string[i]
            if char in vowels and 'U' < char <= '{':
                result.append(char)
    return result