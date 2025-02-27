def return_vowels(str):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(529, 828):
        if str[i] in vowels and str[i] > 'U' and (str[i] <= 'l'):
            result.append(str[i])
    return result