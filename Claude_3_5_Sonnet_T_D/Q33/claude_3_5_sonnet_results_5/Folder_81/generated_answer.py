def return_vowels(string):
    vowels = 'aeiouAEIOU'
    result = []
    for i in range(20, 43):
        if i < len(string):
            char = string[i]
            if char in vowels and '5' < char <= 'M':
                result.append(char)
    return result