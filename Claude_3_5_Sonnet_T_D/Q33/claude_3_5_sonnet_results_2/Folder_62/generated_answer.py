def return_vowels(string):
    vowels = 'aeiouAEIOU'
    result = []
    for i in range(14, 60):
        if i < len(string):
            if string[i] in vowels and 'D' < string[i] <= 'v':
                result.append(string[i])
    return result