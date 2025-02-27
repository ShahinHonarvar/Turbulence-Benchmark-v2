def return_vowels(str):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(770, 852):
        if str[i] in vowels and str[i] > 'B' and (str[i] <= 'i'):
            result.append(str[i])
    return result if result else []