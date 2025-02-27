def return_vowels(str):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(32, 97):
        if str[i] in vowels and str[i] > 'Q' and (str[i] <= ']'):
            result.append(str[i])
    return result