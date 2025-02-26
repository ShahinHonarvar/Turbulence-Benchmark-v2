def return_vowels(string):
    vowels = 'aeiouAEIOU'
    result = []
    for i in range(23, 85):
        if i < len(string):
            if string[i] in vowels and 'W' < string[i] <= 'v':
                result.append(string[i])
    return result