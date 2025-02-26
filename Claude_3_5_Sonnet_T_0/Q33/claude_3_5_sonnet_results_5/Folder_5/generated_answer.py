def return_vowels(string):
    vowels = 'aeiouAEIOU'
    result = []
    for i in range(44, 95):
        if i < len(string):
            char = string[i]
            if char in vowels and '5' < char <= '<':
                result.append(char)
    return result