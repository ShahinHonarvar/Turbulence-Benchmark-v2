def return_vowels(string):
    vowels = 'aeiouAEIOU'
    result = []
    for i in range(22, 82):
        if i < len(string):
            if string[i] in vowels and 'N' < string[i] <= 'o':
                result.append(string[i])
    return result