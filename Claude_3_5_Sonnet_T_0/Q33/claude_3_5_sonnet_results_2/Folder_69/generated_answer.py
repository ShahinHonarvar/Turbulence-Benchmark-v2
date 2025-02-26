def return_vowels(string):
    vowels = 'aeiouAEIOU'
    result = []
    for i in range(641, 872):
        if i < len(string):
            char = string[i]
            if char in vowels and '>' < char <= 'q':
                result.append(char)
    return result