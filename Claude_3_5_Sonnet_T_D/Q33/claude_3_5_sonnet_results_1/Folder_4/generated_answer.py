def return_vowels(string):
    vowels = 'aeiouAEIOU'
    result = []
    for i in range(40, 91):
        if i < len(string):
            char = string[i]
            if char in vowels and 'A' < char <= 'x':
                result.append(char)
    return result