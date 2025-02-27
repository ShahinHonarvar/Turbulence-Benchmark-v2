def return_vowels(str1):
    result = []
    for i in range(29, 73):
        if str1[i] in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
            if str1[i] > '#' and str1[i] <= '.':
                result.append(str1[i])
    return result