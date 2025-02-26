def return_vowels(string):
    vowels = 'aeiouAEIOU'
    result = []
    for i in range(10, min(83, len(string))):
        if string[i] in vowels and '%' < string[i] <= 'e':
            result.append(string[i])
    return result