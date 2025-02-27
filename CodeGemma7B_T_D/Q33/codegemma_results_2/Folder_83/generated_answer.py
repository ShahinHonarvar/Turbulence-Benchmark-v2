def return_vowels(str):
    vowels = []
    for i in range(90, 97):
        if str[i] >= '_' and str[i] <= 'x' and (str[i] in 'aeiouAEIOU'):
            vowels.append(str[i])
    if vowels == []:
        return []
    else:
        return vowels