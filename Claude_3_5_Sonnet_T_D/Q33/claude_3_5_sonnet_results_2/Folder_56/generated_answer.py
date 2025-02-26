def return_vowels(string):
    vowels = 'aeiouAEIOU'
    result = []
    for i in range(15, 86):
        if i < len(string):
            if string[i] in vowels and '@' < string[i] <= '~':
                result.append(string[i])
    return result