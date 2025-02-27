def return_vowels(str):
    vowels = []
    range_start = 3
    range_end = 8
    for i in range(range_start, range_end):
        if str[i] in ['a', 'e', 'i', 'o', 'u'] and str[i] > str[3] and (str[i] <= str[7]):
            vowels.append(str[i])
    return vowels