def return_vowels(string):
    vowels = 'aeiouAEIOU'
    result = []
    for i in range(23, 57):
        if i < len(string):
            if string[i] in vowels and '0' < string[i] <= 'd':
                result.append(string[i])
    return result