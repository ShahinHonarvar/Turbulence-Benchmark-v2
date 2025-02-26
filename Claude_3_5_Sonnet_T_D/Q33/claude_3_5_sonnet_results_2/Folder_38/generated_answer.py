def return_vowels(string):
    vowels = 'aeiouAEIOU'
    result = []
    for i in range(17, 65):
        if i < len(string):
            if string[i] in vowels and 'U' < string[i] <= '{':
                result.append(string[i])
    return result