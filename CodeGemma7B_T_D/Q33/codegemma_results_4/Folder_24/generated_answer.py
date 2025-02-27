def return_vowels(str):
    vowels = ['a', 'e', 'i', 'o', 'u']
    len_of_string = len(str)
    result = []
    for i in range(23, 57):
        if i >= len_of_string:
            break
        for j in vowels:
            if j > str[i]:
                continue
            elif j <= 'd' and j in str[i]:
                result.append(j)
    return result