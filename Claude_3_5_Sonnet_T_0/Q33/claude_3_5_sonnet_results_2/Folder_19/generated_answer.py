def return_vowels(string):
    vowels = 'aeiouAEIOU'
    result = []
    for i in range(51, 77):
        if i < len(string):
            if string[i] in vowels and '4' < string[i] <= '=':
                result.append(string[i])
    return result