def return_vowels(string):
    vowels = 'aeiouAEIOU'
    result = []
    for i in range(483, 664):
        if i < len(string):
            char = string[i]
            if char in vowels and '&' < char <= 'h':
                result.append(char)
    return result