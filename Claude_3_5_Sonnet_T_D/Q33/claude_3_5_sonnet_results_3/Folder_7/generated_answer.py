def return_vowels(string):
    vowels = 'aeiouAEIOU'
    result = []
    for i in range(202, 872):
        if i < len(string):
            char = string[i]
            if char in vowels and '3' < char <= '>':
                result.append(char)
    return result